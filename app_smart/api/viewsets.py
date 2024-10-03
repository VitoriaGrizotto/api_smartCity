from django.contrib.auth.models import User
from rest_framework import generics, permissions
from app_smart.api import serializers 
from rest_framework.response import Response 
from rest_framework import status
from ..models import Sensor, TemperaturaData 
from rest_framework import viewsets
from app_smart.api.filters import SensorFilter
from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.generics import CreateUserAPIViewSet

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorFilter

class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    serializer_class = serializers.TemperaturaDataSerializer
    permission_classes = [permissions.IsAuthenticated]

