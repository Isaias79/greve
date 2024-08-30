from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto, Fornecedor
from django.db.models import Count

def resultado_produtos_relacionamentos(request):
    Fornecedor = Fornecedor.object.get(id=8)
    Produto = Fornecedor.produto_set.all()
    Produto = Fornecedor.produtos.all() ## RELATED NAME
    return HttpResponse("olá") 

def cadastrar(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        qtd = request.POST.get('quantidade')
        
        novo_produto = Produto()
        novo_produto.nome = nome
        novo_produto.valor = preco
        novo_produto.estoque = qtd
        novo_produto.save()

    return render(request, 'loja/formcad.html', {})

def home(request):
    return render(request, 'loja/home.html', {})

def pesquisar(request):

    if request.method == 'POST':
        print("Chegou a pesquisa!")
        pesquisa = request.POST.get('pesquisa') ## name do forms no template
        print(pesquisa)
        resultado = Produto.objects.filter(nome__contains=pesquisa)
        return render(request, 'loja/pesquisa.html', {'nome':'Marcos', 'resultado':resultado})
    #resultado = Produto.objects.all()
    # resultado = Produto.objects.filter(nome__exact='xi')
    # resultado = Produto.objects.exclude(nome="Abacaxi")
    # filter(nome__contains='banana',preco=20)
    # resultado = Produto.objects.filter(nome__contains='banana',preco=20, quantidade__gt=0)
    resultado = Produto.objects.filter(nome='abacate')


    
    # exclude() ##Todo mundo menos esse
    # resultado = Produto.objects.get(id=1)
    # print(resultado)
    print("Opa chegou")
    # return HttpResponse("Estou no atualizar")
    return HttpResponse(resultado)

# Create your views here.
