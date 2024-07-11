from django.shortcuts import render
from django.http import HttpResponse
from .models import Produto
from django.db.models import Count


def pesquisar(request):
    #resultado = Produto.objects.all()
    # resultado = Produto.objects.filter(nome__exact='xi')
    # resultado = Produto.objects.exclude(nome="Abacaxi")
    q = Blog.objects.annotate(Count("entry"))
    
    # exclude() ##Todo mundo menos esse
    # resultado = Produto.objects.get(id=1)
    print(resultado)
    print("Opa chegou")
    # return HttpResponse("Estou no atualizar")
    return HttpResponse(q[0].entry__count)

# Create your views here.
