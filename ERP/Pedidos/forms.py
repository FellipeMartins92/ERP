from django import forms
from .models import *

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedidos
        fields = ['Cliente', 'Data_Entrega']
        
        widgets = {
            'Cliente': forms.Select(attrs={'class': 'form-select'}),
            'Data_Entrega': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

class Itens_PedidoForm(forms.ModelForm):
    class Meta:
        model = Itens_Pedido
        fields = ['Produto','Valor','Quantidade']

        widgets = {
            'Produto': forms.Select(attrs={'class': 'form-select'}),
            'Valor': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite o valor do produto'}),
            'Quantidade': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Digite a quantidade do produto'}),
        }
