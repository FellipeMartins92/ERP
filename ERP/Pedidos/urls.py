from django.urls import path
from . import views

urlpatterns = [
    # Pedidos
    path('Cadastro_Pedido/', views.Cadastro_Pedido, name='Cadastro_Pedido'),
    path('Salvar_Pedido/', views.Salvar_Pedido, name='Salvar_Pedido'),
    path('Listar_Pedidos/', views.Listar_Pedidos, name='Listar_Pedidos'),
    path('Excluir_Pedido/<int:Id>/', views.Excluir_Pedido, name='Excluir_Pedido'),

    #Itens de Pedido
    path('Adicionar_Itens_Do_Pedido/<int:Id>', views.Adicionar_Itens_Do_Pedido, name='Adicionar_Itens_Do_Pedido'),
    path('Salvar_Itens_Do_Pedido/<int:pedido_id>/', views.Salvar_Itens_Do_Pedido, name='Salvar_Itens_Do_Pedido'),
    path('Excluir_Item_Do_Pedido/<int:Item_pedido_id>/', views.Excluir_Item_Do_Pedido, name='Excluir_Item_Do_Pedido'),
    
]
