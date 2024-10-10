from django.contrib.auth.models import User
from rest_framework import generics, permissions, status
from rest_framework.response import Response 
from rest_framework import viewsets
from app_smart.api import serializers
from app_smart.models import Sensor, TemperaturaData
from app_smart.api.serializers import TemperaturaDataSerializer
# from app_smart.api.viewsets import TemperaturaDataViewSet

import csv

class CreateUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = serializers.SensorSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # Nova rota para upload de CSV
    def upload(self, request):
        if 'file' in request.FILES:
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                try:
                    # Lê o conteúdo do arquivo CSV
                    reader = csv.DictReader(file.read().decode('utf-8').splitlines(), delimiter=',')
                    for row in reader:
                        # Verifique se os campos necessários estão presentes
                        Sensor.objects.create(
                            tipo=row['tipo'],
                            unidade_medida=row.get('unidade_medida', None),
                            latitude=float(row['latitude'].replace(',', '.')),
                            longitude=float(row['longitude'].replace(',', '.')),
                            localizacao=row['localizacao'],
                            responsavel=row.get('responsavel', ''),
                            status_operacional=row['status_operacional'].strip().lower() == 'true',
                            observacao=row.get('observacao', ''),
                            mac_address=row.get('mac_address', None)
                        )
                    return Response({'status': 'Dados carregados com sucesso!'}, status=status.HTTP_201_CREATED)
                except ValueError as e:
                    return Response({'error': 'Erro ao converter dados: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
                except Exception as e:
                    return Response({'error': 'Erro ao processar o arquivo: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Formato de arquivo inválido. Somente CSV é aceito.'}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({'error': 'Arquivo não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)
    
class TemperaturaDataViewSet(viewsets.ModelViewSet):
    queryset = TemperaturaData.objects.all()
    # serializer_class = serializers.TemperaturaDataSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def upload(self, request):
        if 'file' in request.FILES:
            file = request.FILES['file']
            if file.name.endswith('.csv'):
                try:
                    print("entrou")
                    reader = csv.DictReader(file.read().decode('utf-8').splitlines(), delimiter=',')
                    for row in reader:
                        sensor = Sensor.objects.get(id=row['sensor_id'])  # Busca o sensor pelo ID
                        # print(sensor)
                        # Verifica se a chave 'tipo' está presente na linha
                        tipo = row.get('tipo', None)  # Retorna None se a chave não existir

                        TemperaturaData.objects.create(
                            sensor=sensor,
                            valor=float(row['valor'].replace(',', '.')),
                            timestamp=row['timestamp'],
                            tipo=tipo
                        )
                    return Response({'status': 'Temperaturas carregadas com sucesso!'}, status=status.HTTP_201_CREATED)
                except Exception as e:
                    return Response({'error': 'Erro ao processar o arquivo: {}'.format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Formato de arquivo inválido. Somente CSV é aceito.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Arquivo não encontrado.'}, status=status.HTTP_400_BAD_REQUEST)

