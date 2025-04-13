from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


#Clientes
def Cadastro_Clientes(request):
    tipos_cliente = Tipo_Cliente.objects.all()
    classes_cliente = Classe_Cliente.objects.all()
    enderecos = Endereco.objects.all()
    return render(request,"Clientes/Cadastro_Cliente.html",{"tipos_cliente": tipos_cliente,"classes_cliente": classes_cliente,"enderecos": enderecos})

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

def Listar_Clientes(request):
    clientes = Cliente.objects.select_related(
        'Tipo_Cliente', 'Classe_Cliente', 'Endereco_Cliente'
    ).order_by('Nome')  # Ordena por nome, por exemplo

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

#Endereco

def Cadastro_Endereco(request):
    return render(request,"Endereco/Cadastro_Endereco.html")

def Salvar_Endereco(request):
    if request.method == 'POST':
        form = EnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EnderecoForm()    

    return render(request, 'Endereco/Cadastro_Endereco.html', {'form': form})