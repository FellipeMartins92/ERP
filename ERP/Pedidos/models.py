from django.db import models
from Clientes.models import *
from Produtos.models import *
from django.utils.timezone import now

class Pedidos(models.Model):
    Cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE, related_name="Cliente")
    Data_Entrega = models.DateField()
    Data_Cadastro = models.DateField(default=now)
    Valor_Total = models.FloatField(default=0)    

class Itens_Pedido(models.Model):
    Pedido = models.ForeignKey(Pedidos, on_delete=models.CASCADE, related_name="Pedido")
    Produto = models.ForeignKey(Produtos, on_delete=models.CASCADE, related_name="itens_produto")
    Valor = models.FloatField()
    Quantidade = models.FloatField()

    def SubTotal(self):
        return self.Valor * self.Quantidade
    
    def __str__(self):
        return f"{self.Quantidade}x {self.Produto.Descricao} - R$ {self.SubTotal():.2f}"


