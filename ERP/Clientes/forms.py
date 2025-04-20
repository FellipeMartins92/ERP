from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'Tipo_Cliente', 'CEP', 'Rua', 'Bairro', 'Estado', 'Pais',
                  'Classe_Cliente', 'Aniversario_Cliente', 'Ativo']
        
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do cliente'}),
            'Tipo_Cliente': forms.Select(attrs={'class': 'form-select'}),
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'Rua': forms.TextInput(attrs={'class': 'form-control'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
            'Classe_Cliente': forms.Select(attrs={'class': 'form-select'}),
            'Aniversario_Cliente': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'Ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class Tipo_ClienteForm(forms.ModelForm):
    class Meta:
        model = Tipo_Cliente
        fields = ['Descricao']
        widgets = {
            'Descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }