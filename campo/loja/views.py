from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from django.db.models import Count


def pesquisar(request):
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
