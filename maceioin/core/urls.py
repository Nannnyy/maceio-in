from django.urls import path
from core.views import home, perfil, listar, adicionar, cadastrar, atualizar, editar, deletar

urlpatterns = [
    path('', home, name="home"),
    path('perfil/', perfil, name="perfil"),
    path('listar', listar, name="listar"),
    path('adicionar', adicionar, name="adicionar"),
    path('cadastrar', cadastrar, name="cadastrar"),
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('deletar/<int:id>', deletar, name="deletar"),
]