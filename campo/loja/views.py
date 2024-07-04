from django.shortcuts import render
from django.http import HttpResponse

def pesquisar(request):
    print("Opa chegou")
    return HttpResponse("Estou no atualizar")

# Create your views here.
