from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from rest_framework.response import Response
from .serializer import UserSerializer
User=get_user_model()
# Create your views here.
class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        try:
            user=User.objects.get(username=username, password=password)
            authenticate(user)
            refresh = RefreshToken.for_user(user)
            serializer=UserSerializer(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token),"user":serializer.data}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)    
        
        