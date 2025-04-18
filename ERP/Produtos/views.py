from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *


#Tamanhos
def Cadastro_Tamanhos(request):
    return render(request,"Tamanho/Cadastro_Tamanhos.html")    

def Salvar_Tamanhos(request):
    if request.method == 'POST':
        form = TamanhoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = TamanhoForm()    

    return render(request, 'Tamanho/Cadastro_Tamanhos.html', {'form': form})    

#Cores
def Cadastro_Cores(request):
    return render(request,"Cor/Cadastro_Cores.html")    

def Salvar_Cores(request):
    if request.method == 'POST':
        form = CorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CorForm()    

    return render(request, 'Cor/Cadastro_Cores.html', {'form': form})

#Categorias    
def Cadastro_Categorias(request):
    return render(request,"Categorias/Cadastro_Categorias.html")    

def Salvar_Categorias(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = CategoriaForm()    

    return render(request, 'Categorias/Cadastro_Categorias.html', {'form': form})

#Produtos
def Cadastro_Produtos(request):
    tamanhos = Tamanho.objects.all()
    categorias = Categoria.objects.all()
    cores = Cor.objects.all()

    return render(request, 'Produtos/Cadastro_Produtos.html', {'tamanhos': tamanhos,'categorias': categorias,'cores': cores,})    

def Salvar_Produtos(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = ProdutoForm()    

    return render(request, 'Produtos/Cadastro_Produtos.html', {'form': form})

def Listar_Produtos(request):
    produtos = Produtos.objects.all()
    return render(request, 'Produtos/Listar_Produtos.html', {'produtos': produtos})


def Editar_Produtos(request, Id):
    produtos = get_object_or_404(Produtos.objects.select_related('Tamanho','Categoria', 'Cor'), id=Id)
    tamanhos = Tamanho.objects.all()
    categorias = Categoria.objects.all()
    cores = Cor.objects.all()
    return render(request, "Produtos/Editar_Produtos.html", {
        'produto': produtos,
        'tamanhos': tamanhos,
        'categorias': categorias,
        'cores': cores
    })

def Excluir_Produto(request, Id):
    produtos = get_object_or_404(Produtos, id=Id)
    produtos.delete()
    return redirect('Listar_Produtos')

def Salvar_Produto_Editado(request,Id):
    produtos = get_object_or_404(Produtos, id=Id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            return redirect('Listar_Produtos')
    else:
        form = ProdutoForm(instance=produtos)

    return render(request, "Produtos/Listar_Produtos.html")

# Create your views here.
