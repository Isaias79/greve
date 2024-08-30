from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('pesquisar/', views.pesquisar, name='pesquisar'),
    path('home/', views.home, name='home'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('resultado_produtos_relacionamentos/', views.resultado_produtos_relacionamentos, name='resultado_produtos_relacionamentos'),
]

# nome__contains='anja' #Laranja
# id__in[1,2,3] Pega esses ids
# preco__gt(50) Maiores que 50
# preco__gte(50) Maior igual que 50