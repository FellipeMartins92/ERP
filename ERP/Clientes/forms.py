from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Nome', 'Tipo_Cliente', 'Endereco_Cliente',
                  'Classe_Cliente', 'Aniversario_Cliente', 'Ativo']
        
        widgets = {
            'Nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome do cliente'}),
            'Tipo_Cliente': forms.Select(attrs={'class': 'form-select'}),
            'Endereco_Cliente': forms.Select(attrs={'class': 'form-select'}),
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

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['CEP','Rua','Bairro','Estado','Pais']
        widgets = {
            'CEP': forms.TextInput(attrs={'class': 'form-control'}),
            'Rua': forms.TextInput(attrs={'class': 'form-control'}),
            'Bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'Estado': forms.TextInput(attrs={'class': 'form-control'}),
            'Pais': forms.TextInput(attrs={'class': 'form-control'}),
        }    
