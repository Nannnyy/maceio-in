
from django.shortcuts import redirect, render
from .models import Funcionario

def home(request):
    return render(request, 'index.html')

def listar(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios.html', {"funcionarios": funcionarios})

def cadastrar(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    setor = request.POST.get('setor')
    
    Funcionario.objects.create(nome=nome, email=email, setor=setor)
    pessoas = Funcionario.objects.all
    return render(request, 'index.html', {'pessoas' : pessoas})

def editar(request, id):
    # pegar usuario do banco
    funcionario = Funcionario.objects.get(id=id)
    return render(request, 'update_funcionario.html', {'funcionario' : funcionario})

def atualizar(request, id):
    if request.method == "POST":
        funcionario = Funcionario.objects.get(id=id)
        
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        setor = request.POST.get('setor')
        
        funcionario.nome = nome
        funcionario.email = email
        funcionario.setor = setor
        
        funcionario.save()
        
    return redirect(listar)

def deletar(request, id):
    pessoa = Funcionario.objects.get(id=id)
    pessoa.delete()
    return redirect(listar)

