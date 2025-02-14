from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages 
from core.views import home as core_home


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        if not username or not email or not senha:
            messages.error(request, "Todos os campos são obrigatórios!")
            return render(request, 'cadastro.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Usuário já existe!")
            return render(request, 'cadastro.html')
        
                # Criando usuário
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect("login") 

    return render(request, 'cadastro.html')



def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')

        if not username or not senha:
            messages.error(request, "Preencha todos os campos!")
            return render(request, 'login.html')

        user = authenticate(username=username, password=senha)

        if user:
            auth_login(request, user)
            return redirect(core_home)
        else:
            messages.error(request, "Usuário ou senha inválidos!")
            return render(request, 'login.html')

    return render(request, 'login.html')
