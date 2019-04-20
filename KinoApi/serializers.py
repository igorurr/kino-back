from rest_framework import serializers
from . import models

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=50)

class EmailSerializer(serializers.Serializer):
    email = serializers.EmailField()