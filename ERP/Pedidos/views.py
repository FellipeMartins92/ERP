from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from Clientes.models import *
from django.contrib import messages

# Create your views here.

#Pedidos

def Cadastro_Pedido(request):
    clientes = Cliente.objects.all()
    return render(request,"Pedidos/Cadastro_Pedido.html",{"clientes": clientes})

def Salvar_Pedido(request):
    print(request.method)
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            pedido = form.save()
            return redirect('Adicionar_Itens_Do_Pedido', Id=pedido.id)
    else:
        form = PedidoForm()

    return render(request, 'Pedidos/Cadastro_Pedido.html', {'form': form})

def Listar_Pedidos(request):
    pedidos = Pedidos.objects.all()

    return render(request, "Pedidos/Listar_Pedidos.html", {"pedidos": pedidos})

#Itens do Pedido

def Adicionar_Itens_Do_Pedido(request, Id):
    pedido = get_object_or_404(Pedidos, id=Id)
    itens_do_pedido = Itens_Pedido.objects.filter(Pedido=pedido)
    produtos = Produtos.objects.all()

    return render(request, "Itens_Do_Pedido/Adicionar_Itens_Do_Pedido.html", {
        "pedido": pedido,
        "itens_do_pedido": itens_do_pedido,
        "produtos": produtos
    })

def Excluir_Pedido(request, Id):
    pedido = get_object_or_404(Pedidos, id=Id)
    pedido.delete()
    return redirect('Listar_Pedidos')    

def Salvar_Itens_Do_Pedido(request, pedido_id):
    if (request.method == 'POST'):
        produto = get_object_or_404(Produtos, id=int(request.POST.get('Produto')))  

        valor = float(request.POST.get('Valor'))
        quantidade = float(request.POST.get('Quantidade'))        

        pedido = Pedidos.objects.filter(id=pedido_id).first()
        item_pedido = Itens_Pedido.objects.create(
            Pedido=pedido,
            Produto=produto,
            Valor=valor,
            Quantidade=quantidade            
        )

        pedido.Valor_Total += item_pedido.SubTotal()
        pedido.save()

        ##return redirect('Adicionar_Itens_Pedido', id=pedido_id)
        return redirect('Listar_Pedidos')

    return redirect('Listar_Pedidos')


