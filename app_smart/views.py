from django.http import HttpResponse
import csv
from django.shortcuts import render, redirect
from django.conf import settings
from .models import Sensor
from rest_framework.parsers import MultiPartParser, FormParser
from .forms import CSVUploadForm
 
 
def abre_index(request):
    mensagem = "OLÁ TURMA, SEJAM FELIZES SEMPRE!"
    return HttpResponse(mensagem)
 
 
def upload_csv_view(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
       
        if form.is_valid():
            csv_file = request.FILES['file']
           
            # Verifica se o arquivo tem a extensão correta
            if not csv_file.name.endswith('.csv'):
                form.add_error('file', 'Este não é um arquivo CSV válido.')
            else:
                # Processa o arquivo CSV
                file_data = csv_file.read().decode('ISO-8859-1').splitlines()
                reader = csv.DictReader(file_data, delimiter=',')  
               
                for row in reader:
                    try:
                        Sensor.objects.create(
                            tipo=row['tipo'],
                            unidade_medida=row['unidade_medida'] if row['unidade_medida'] else None,
                            latitude=float(row['latitude'].replace(',', '.')),
                            longitude=float(row['longitude'].replace(',', '.')),
                            localizacao=row['localizacao'],
                            responsavel=row['responsavel'] if row['responsavel'] else '',
                            status_operacional=True if row['status_operacional'] == 'True' else False,
                            observacao=row['observacao'] if row['observacao'] else '',
                            mac_address=row['mac_address'] if row['mac_address'] else None
                        )
                    except KeyError as e:
                        print(f"Chave não encontrada: {e} na linha: {row}")  # Exibe o erro e a linha problemática    

        return render(request, 'app_smart/upload.html', {'form': form})  # Caminho correto
    else:
        form = CSVUploadForm()
 
    return render(request, 'app_smart/upload.html', {'form': form})