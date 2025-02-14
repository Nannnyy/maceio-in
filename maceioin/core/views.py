
from django.shortcuts import redirect, render
from .models import Funcionario
from django.contrib.auth import logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')


@login_required(login_url="/auth/login")
def perfil(request):
    return render(request, 'perfil.html', {'user': request.user})


@login_required(login_url="/auth/login")
def listar(request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionarios.html', {"funcionarios": funcionarios})
    
    
def adicionar(request):
    return render(request, 'cadastrar_funcionario.html')


def cadastrar(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    setor = request.POST.get('setor')

    if not nome or not email or not setor:
        messages.error(request, "Preencha todos os campos!")
        return render(request, 'cadastrar_funcionario.html')
    
    funcionario = Funcionario.objects.create(nome=nome, email=email, setor=setor)
    funcionario.save()
    return redirect(listar)


def editar(request, id):
    funcionario = Funcionario.objects.get(id=id)
    return render(request, 'update_funcionario.html', {'funcionario' : funcionario})


def atualizar(request, id):
    if request.method == "POST":
        funcionario = Funcionario.objects.get(id=id)
        
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        setor = request.POST.get('setor')
        
        if not nome or not email or not setor:
            messages.error(request, "Preencha todos os campos!")
            return render(request, 'update_funcionario.html', {'funcionario' : funcionario})
        
        funcionario.nome = nome
        funcionario.email = email
        funcionario.setor = setor
        
        funcionario.save()
        
    return redirect(listar)


def deletar(request, id):
    pessoa = Funcionario.objects.get(id=id)
    pessoa.delete()
    return redirect(listar)


def custom_logout(request):
    logout(request)
    return redirect(home)