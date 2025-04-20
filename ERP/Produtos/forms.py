from django import forms
from .models import *

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produtos
        fields = ['Descricao', 'Referencia', 'Tamanho', 'Categoria', 'Cor',]
        
        widgets = {
            'Descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição do produto'}),
            'Referencia': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a referência do produto'}),
            'Tamanho': forms.Select(attrs={'class': 'form-select'}),
            'Categoria': forms.Select(attrs={'class': 'form-select'}),
        }

class TamanhoForm(forms.ModelForm):
    class Meta:
        model = Tamanho
        fields = ['Descricao','Sigla']

        widgets = {
            'Descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição do tamanho'}),
            'Sigla': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a sigla do tamanho'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['Descricao']

        widgets = {
           'Descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição da Categoria'}), 
        }

class CorForm(forms.ModelForm):
    class Meta:
        model = Cor
        fields = ['Descricao']

        widgets = {
            'Descricao': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite a descrição da Cor'}),
        }