from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


#Clientes
def Cadastro_Clientes(request):
    tipos_cliente = Tipo_Cliente.objects.all()
    classes_cliente = Classe_Cliente.objects.all()
    return render(request,"Clientes/Cadastro_Cliente.html",{"tipos_cliente": tipos_cliente,"classes_cliente": classes_cliente})

def Salvar_Cliente(request):
    print(request.method)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('Listar_Clientes')
    else:
        form = ClienteForm()

    return render(request, 'Clientes/Cadastro_Cliente.html', {'form': form})

def Editar_Clientes(request, Id):
    cliente = get_object_or_404(Cliente.objects.prefetch_related('Tipo_Cliente', 'Classe_Cliente'), id=Id)
    tipos_cliente = Tipo_Cliente.objects.all()
    classes_cliente = Classe_Cliente.objects.all()
    return render(request, "Clientes/Editar_Clientes.html", {
        'cliente': cliente,
        'tipos_cliente': tipos_cliente,
        'classes_cliente': classes_cliente,
    })

def Excluir_Cliente(request, Id):
    cliente = get_object_or_404(Cliente, id=Id)
    cliente.delete()
    return redirect('Listar_Clientes')

def Salvar_Cliente_Editado(request,Id):
    cliente = get_object_or_404(Cliente, id=Id)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('Listar_Clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, "Clientes/Listar_Clientes.html")

def Listar_Clientes(request):
    clientes = Cliente.objects.select_related(
        'Tipo_Cliente', 'Classe_Cliente'
    ).order_by('Nome') 

    return render(request, "Clientes/Listar_Clientes.html", {"clientes": clientes})

#Tipo Cliente

def Cadastro_Tipos_Cliente(request):
    return render(request,"Tipo_Cliente/Cadastro_Tipo_Cliente.html")

def Salvar_Tipos_Cliente(request):
    if request.method == 'POST':
        form = Tipo_ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = Tipo_ClienteForm()    

    return render(request, 'Tipo_Cliente/Cadastro_Tipo_Cliente.html', {'form': form})
