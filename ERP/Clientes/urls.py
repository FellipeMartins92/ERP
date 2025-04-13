from django.urls import path
from . import views

urlpatterns = [
    #Clientes
    path('Cadastro_Clientes/', views.Cadastro_Clientes, name='Cadastro_Clientes'),
    path('Salvar_Clientes/', views.Salvar_Cliente, name='Salvar_Clientes'),
    path('Listar_Clientes/', views.Listar_Clientes, name='Listar_Clientes'),

    #Tipos_Cliente
    path('Cadastro_Tipos_Cliente/', views.Cadastro_Tipos_Cliente, name='Cadastro_Tipos_Cliente'),
    path('Salvar_Tipos_Cliente/', views.Salvar_Tipos_Cliente, name='Salvar_Tipos_Cliente'),

    #Endereco
    path('Cadastro_Endereco/', views.Cadastro_Endereco, name='Cadastro_Endereco'),
    path('Salvar_Endereco/', views.Salvar_Endereco, name='Salvar_Endereco'),
]
