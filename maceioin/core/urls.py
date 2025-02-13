from django.urls import path
from core.views import home, perfil, listar, adicionar, cadastrar, atualizar, editar, deletar, custom_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home"),
    path('perfil/', perfil, name="perfil"),
    path('listar', listar, name="listar"),
    path('adicionar', adicionar, name="adicionar"),
    path('cadastrar', cadastrar, name="cadastrar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('deletar/<int:id>', deletar, name="deletar"),
    path('logout/', custom_logout, name="logout"),
]