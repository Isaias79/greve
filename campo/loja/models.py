from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    
    def __str__(self):
        return self.nome
    #quantidade = 

# COLOCAR FLOAT DA PROBLEMA NA PROGAMAÇÃO
# Create your models here.
