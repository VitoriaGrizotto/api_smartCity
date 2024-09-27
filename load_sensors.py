import os
import django
import csv
 
# Configure o ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_city.settings')
django.setup()
 
from app_smart.models import Sensor
 
def load_sensors_from_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')  # Usando vírgula como delimitador
       
        for row in reader:
            row = {k.strip(): v for k, v in row.items()}  # Remove espaços em branco
           
            Sensor.objects.create(
                tipo=row['tipo'],
                unidade_medida=row['unidade_medida'] if row['unidade_medida'] else None,
                latitude=float(row['latitude'].replace(',', '.')),
                longitude=float(row['longitude'].replace(',', '.')),
                localizacao=row['localizacao'],
                responsavel=row['responsavel'] if row['responsavel'] else '',
                status_operacional=row['status_operacional'].strip() == 'True',  # Verificando status operacional
                observacao=row['observacao'] if row['observacao'] else '',
                mac_address=row['mac_address'] if row['mac_address'] else None
            )
    print('Dados carregados com sucesso!!!')
 
if __name__ == "__main__":
    # Caminho para o arquivo
    base_dir = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório do script
    file_path = os.path.join(base_dir, 'dados', 'sensor_data.csv')
    load_sensors_from_csv(file_path)