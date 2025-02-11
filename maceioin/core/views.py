
from django.shortcuts import redirect, render
from .models import Funcionario

def home(request):
    pessoas = Funcionario.objects.all()
    return render(request, 'index.html', {"pessoas": pessoas})

def cadastrar(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    setor = request.POST.get('setor')
    
    Funcionario.objects.create(nome=nome, email=email, setor=setor)
    pessoas = Funcionario.objects.all
    return render(request, 'index.html', {'pessoas' : pessoas})

def editar(request, id):
    # pegar usuario do banco
    pessoa = Funcionario.objects.get(id=id)
    return render(request, 'update.html', {'pessoa' : pessoa})

def atualizar(request, id):
    pessoa = Funcionario.objects.get(id=id)
    
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    setor = request.POST.get('setor')
    
    pessoa.nome = nome
    pessoa.email = email
    pessoa.setor = setor
    pessoa.save()
    
    return redirect(home)

def deletar(request, id):
    pessoa = Funcionario.objects.get(id=id)
    pessoa.delete()
    return redirect(home)
# def cadastrar(request):
#     if request.method == 'POST':
#         try:
#             dados = json.loads(request.body)
            
#             funcionario = cadastrar_funcionario(
#                 nome=dados.get('nome'),
#                 email=dados.get('email'),
#                 setor=dados.get('setor')
#             )
            
#             return JsonResponse({"mensagem": "Funcionário cadastrado com sucesso!", "id": funcionario.id}, status=201)
        
#         except Exception as e:
#             return JsonResponse({"erro": str(e)}, status=400)
            

