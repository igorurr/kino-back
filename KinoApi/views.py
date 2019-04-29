from KinoApi.models import CustomUser
from rest_framework.parsers import JSONParser
from KinoApi.serializers import UserSerializer, EmailSerializer
from django.views.generic.base import TemplateView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.decorators import api_view


class UserCountView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk=None):
        user_count = CustomUser.objects.count()
        content = {'user_count': user_count}

        return Response( content, content_type='application/json' )

class UserAuthView(ObtainAuthToken):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer, )

    def post(self, request, pk=None):
        errors = {}
        
        try:
            email = request.data['email']
        except:
            errors['email'] = 'is required'
        
        try:
            password = request.data['password']
        except:
            errors['password'] = 'is required'

        if len(errors.keys()) > 0:
            return Response(
                errors, 
                status=status.HTTP_400_BAD_REQUEST, 
                content_type='application/json' 
            )

        try:
            user = CustomUser.objects.get(email=email)
        except Exception as error:
            print(error)
            return Response(
                {'email': 'юзера с таким emailом не существует'}, 
                status=status.HTTP_403_FORBIDDEN, 
                content_type='application/json' 
            )

        try:
            valid = user.check_password(password)
            if not valid:
                raise ValueError("Password Incorrect")
        except Exception as error:
            print(error)
            return Response(
                {'password': 'неверный пароль'}, 
                status=status.HTTP_403_FORBIDDEN, 
                content_type='application/json' 
            )

        token, created = Token.objects.get_or_create(user=user)
        content = {
            'token': token.key,
            'user': {
                'username': user.username,
                'id': user.pk,
                'email': user.email
            }
        }
        return Response(
            content, 
            status=status.HTTP_201_CREATED, 
            content_type='application/json' 
        )

class UserRegistarationView(APIView):
    parser_classes = (JSONParser,)
    renderer_classes = (JSONRenderer, )

    def post(self, request, pk=None):
        try:
            data = {
                'email': request.data.get('email'),
                'username': request.data.get('username'),
                'password': request.data.get('password')
            }
        except:
            return Response(
                {'err': 'не передано одно из полей'}, 
                status=status.HTTP_400_BAD_REQUEST, 
                content_type='application/json' 
            )
        
        serialized = UserSerializer(data=data)

        if serialized.is_valid():
            try:
                user = CustomUser.objects.create_user(
                    serialized.data['username'],
                    serialized.data['email'],
                    serialized.data['password']
                )
            except Exception as error:
                print(error)
                return Response(
                    {'err': 'юзер уже существует'}, 
                    status=status.HTTP_400_BAD_REQUEST, 
                    content_type='application/json' 
                )
            token, created = Token.objects.get_or_create(user=user)
            content = {
                'token': token.key,
                'user': {
                    'username': user.username,
                    'id': user.pk,
                    'email': user.email
                }
            }
            return Response(
                content, 
                status=status.HTTP_201_CREATED, 
                content_type='application/json' 
            )
        else:
            return Response(
                serialized._errors, 
                status=status.HTTP_400_BAD_REQUEST, 
                content_type='application/json' 
            )


class UserRestorePassView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk=None):
        user_count = CustomUser.objects.count()
        content = {'user_count': user_count}

        response = Response()
        response['Content-Type'] = 'application/json'
        return Response(content)

class UserMeView(ObtainAuthToken):
    renderer_classes = (JSONRenderer, )

    def get(self, request):
        #print( 
        #    request.query_params.get('id'),
        #    request.META['HTTP_AUTHORIZATION']
        #)

        if not('HTTP_AUTHORIZATION' in request.META):
            return Response(
                {'token': 'need this field'}, 
                status=status.HTTP_403_FORBIDDEN, 
                content_type='application/json' 
            )

        tokenValue = request.META['HTTP_AUTHORIZATION'].split()[1]
        try:
            token = Token.objects.get(key=tokenValue)
        except:
            return Response(
                {'token': 'user this token not found'}, 
                status=status.HTTP_403_FORBIDDEN, 
                content_type='application/json' 
            )

        user = CustomUser.objects.get(pk=token.user_id)
        serialisedUser = UserSerializer(data=user)
        serialisedUser.is_valid()

        content = {
            'user': {
                'username': user.username,
                'id': user.id,
                'email': user.email,
            }
        }

        response = Response()
        response['Content-Type'] = 'application/json'
        return Response(content)