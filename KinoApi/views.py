from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import generics

from . import models
from . import serializers

import json

class MeApiView(CreateView):
    template_name = 'me.html'

    def get(self, request, *args, **kwargs):
        return JsonResponse({"key": "value"})

    def post(self, request, *args, **kwargs):
        return JsonResponse({"key": "value"})

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer