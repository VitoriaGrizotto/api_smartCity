from django.db import models

class Sensor(models.Model):
 TIPOS_SENSOR_CHOICES = [
 ('Temperatura', 'Temperatura'),
 ('Umidade', 'Umidade'),
 ('Contador', 'Contador'),
 ('Luminosidade', 'Luminosidade'),
 ]
 tipo = models.CharField(max_length=50, choices=TIPOS_SENSOR_CHOICES)
 mac_address = models.CharField(max_length=20, null=True)
 latitude = models.FloatField()
 longitude = models.FloatField()
 localizacao = models.CharField(max_length=100)
 responsavel = models.CharField(max_length=100)
 #blank = True indica que o campo pode ser deixado em branco,
 #null = True indica que o campo pode ser gravado como null no banco de dados
 #as propriedades dizem que podem não ser preenchido tanto no formulario como no banco de dados
 unidade_medida = models.CharField(max_length=20, blank=True, null=True)
 status_operacional = models.BooleanField(default=True)
 observacao = models.TextField(blank=True)
 def __str__(self):
    return f"{self.tipo} - {self.localizacao}"
