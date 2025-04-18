from django.urls import path
from . import views

urlpatterns = [
    #Produtos
    path('Cadastro_Produtos/', views.Cadastro_Produtos, name='Cadastro_Produtos'),
    path('Salvar_Produtos/', views.Salvar_Produtos, name='Salvar_Produtos'),
    path('Listar_Produtos/', views.Listar_Produtos, name='Listar_Produtos'),
    path('Editar_Produtos/<int:Id>/', views.Editar_Produtos, name='Editar_Produtos'),
    path('Excluir_Produtos/<int:Id>/', views.Excluir_Produto, name='Excluir_Produtos'),
    path('Salvar_Produto_Editado/<int:Id>/', views.Salvar_Produto_Editado, name='Salvar_Produto_Editado'),

    #Categorias
    path('Cadastro_Categorias/', views.Cadastro_Categorias, name='Cadastro_Categorias'),
    path('Salvar_Categorias/', views.Salvar_Categorias, name='Salvar_Categorias'),

    #Tamanhos
    path('Cadastro_Tamanhos/', views.Cadastro_Tamanhos, name='Cadastro_Tamanhos'),
    path('Salvar_Tamanhos/', views.Salvar_Tamanhos, name='Salvar_Tamanhos'),

    #Cores
    path('Cadastro_Cores/', views.Cadastro_Cores, name='Cadastro_Cores'),
    path('Salvar_Cores/', views.Salvar_Cores, name='Salvar_Cores'),
]
