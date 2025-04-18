from django.db import models
from django.utils.timezone import now

class Tipo_Cliente(models.Model):
    Descricao = models.CharField(max_length=255)

class Endereco(models.Model):
    CEP = models.CharField(max_length=20)
    Rua = models.CharField(max_length=100)
    Bairro = models.CharField(max_length=100)
    Estado = models.CharField(max_length=100)
    Pais = models.CharField(max_length=100)

class Classe_Cliente(models.Model):
    Descricao = models.CharField(max_length=50)

class Cliente(models.Model):
    Nome = models.CharField(max_length=150)
    Tipo_Cliente = models.ForeignKey(Tipo_Cliente,on_delete=models.CASCADE, related_name="Tipo")
    Endereco_Cliente = models.ForeignKey(Endereco, on_delete=models.CASCADE, related_name="Endereco")
    Classe_Cliente = models.ForeignKey(Classe_Cliente,on_delete=models.CASCADE, related_name="Tipo")   
    Data_Cadastro = models.DateField(default=now)
    Aniversario_Cliente = models.DateField()
    Ativo = models.BooleanField(default=True)

# Create your models here.
