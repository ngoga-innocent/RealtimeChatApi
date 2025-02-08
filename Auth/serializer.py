from rest_framework import serializers
from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id', 'username','profile', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}
        