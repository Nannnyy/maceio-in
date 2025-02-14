from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login

from core.views import home as core_home


def cadastro(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        
        existing_user = User.objects.filter(username=username).first()
        
        if existing_user:
            return HttpResponse('Usuário já existente')
        
        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        
        return redirect(login)
    return render(request, 'cadastro.html')


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('password')
        
        user = authenticate(username=username, password=senha)
        
        if user:
            auth_login(request, user)
            
            return redirect(core_home)
        else:
            # Eu quero mudar isso aqui
            return HttpResponse('Eamil ou senha invalido')
    return render(request, 'login.html')
