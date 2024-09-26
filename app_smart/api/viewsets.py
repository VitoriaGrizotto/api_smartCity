from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers 
from rest_framework.response import Response 
from rest_framework import status

class CreateUserAPIViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)