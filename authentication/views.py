from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class CreateUser(APIView):
    def post(self, request):
        user = User.objects.create_user(request.data.get('username'), request.data.get('email'), request.data.get('password'))
        user.first_name = request.data.get('first_name')
        user.last_name = request.data.get('last_name')
        user.token = None
        user.save()
        return Response("created user", status=status.HTTP_201_CREATED)
    
    def get(self, request):
        users = User.objects.all()
        print(users)
        return Response("users", status=status.HTTP_200_OK)
    
class AuthUser(APIView):
    def post(self, request, act):
        if act == "login":
            username = request.data.get('username')
            password = request.data.get('password')
            user = authenticate(username=username, password=password)
            print(user)
            if user:
                login(request, user, backend=False)
                return Response("authenticated", status = status.HTTP_200_OK)
            else:
                return Response("not Authenticated", status=status.HTTP_400_BAD_REQUEST)
        elif act == "logout":
            if str(request.user) != "AnonymousUser":
                print(request.user)
                logout(request)
                return Response("Logged Out Successfully", status=status.HTTP_200_OK)
            else:
                return Response("Bad Request", status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request, act):
        return Response('is working...', status=status.HTTP_200_OK)            

