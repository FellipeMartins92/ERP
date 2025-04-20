from django.urls import path
from . import views

urlpatterns = [
    #Clientes
    path('Cadastro_Clientes/', views.Cadastro_Clientes, name='Cadastro_Clientes'),
    path('Salvar_Clientes/', views.Salvar_Cliente, name='Salvar_Clientes'),
    path('Listar_Clientes/', views.Listar_Clientes, name='Listar_Clientes'),
    path('Editar_Clientes/<int:Id>/', views.Editar_Clientes, name='Editar_Clientes'),
    path('Excluir_Cliente/<int:Id>/', views.Excluir_Cliente, name='Excluir_Cliente'),
    path('Salvar_Cliente_Editado/<int:Id>/', views.Salvar_Cliente_Editado, name='Salvar_Cliente_Editado'),

    #Tipos_Cliente
    path('Cadastro_Tipos_Cliente/', views.Cadastro_Tipos_Cliente, name='Cadastro_Tipos_Cliente'),
    path('Salvar_Tipos_Cliente/', views.Salvar_Tipos_Cliente, name='Salvar_Tipos_Cliente'),
]
