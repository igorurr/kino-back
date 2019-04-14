from KinoApi.models import CustomUser
from django.views.generic.base import TemplateView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token

class ApitesterView(TemplateView):
    template_name = "apitester.html"

class UserCountView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk=None):
        user_count = CustomUser.objects.count()
        content = {'user_count': user_count}
        return Response(content)

class UserAuthView(APIView):
    renderer_classes = (JSONRenderer, )

    def post(self, request, pk=None):
        print(request)
        token = Token.objects.create(user=...)
        print(token.key)

        user_count = CustomUser.objects.count()
        content = {'user_count': user_count}
        return Response(content)

class UserRegistarationView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk=None):
        user_count = CustomUser.objects.count()
        content = {'user_count': user_count}
        return Response(content)

class UserRestorePassView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk=None):
        user_count = CustomUser.objects.count()
        content = {'user_count': user_count}
        return Response(content)

class UserMeView(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, pk=None):
        user_count = CustomUser.objects.count()
        content = {'usert': user_count}
        return Response(content)