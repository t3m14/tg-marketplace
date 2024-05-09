from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response

# CREATE RETRIEV UPDATE DELETE USERS
class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return User.objects.filter(user_id=user_id)
        
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
