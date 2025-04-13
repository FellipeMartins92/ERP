from django.db import models

class Tamanho(models.Model):
    Descricao = models.TextField(max_length=100)
    Sigla = models.TextField(max_length=100)

class Cor(models.Model):
    Descricao = models.TextField(max_length=100)

class Categoria(models.Model):
    Descricao = models.TextField(max_length=100)

class Produtos(models.Model):
    Descricao = models.TextField(max_length=100)
    Referencia = models.TextField(max_length=100)
    Tamanho =  models.ForeignKey(Tamanho, on_delete=models.CASCADE, related_name="Tamanho")
    Categoria =  models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="Categoria")
    Cor = models.ForeignKey(Cor, on_delete=models.CASCADE, related_name="Cor")
    Valor = models.DecimalField(max_digits=10, decimal_places=2)
