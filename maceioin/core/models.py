from django.db import models

class Funcionario(models.Model):
    
    SETORES = [
        ('Contabilidade', 'Contabilidade'),
        ('Financeiro', 'Financeiro'),
        ('Atendimento', 'Atendimento'),
        ('Orçamento', 'Orçamento'),
        ('TI', 'TI')
    ]
    
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    setor = models.CharField(max_length=100, choices=SETORES)
    
    
    def __str__(self):
        return f"{self.nome} - {self.setor}"