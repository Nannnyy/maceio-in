from django.urls import path
from core.views import home, cadastrar, atualizar, editar, deletar

urlpatterns = [
    path('', home),
    path('cadastrar', cadastrar, name="cadastrar"),
    # Para dizer quer recebe um parâmetro
    path('editar/<int:id>', editar, name="editar"),
    path('atualizar/<int:id>', atualizar, name="atualizar"),
    path('deletar/<int:id>', deletar, name="deletar"),
]