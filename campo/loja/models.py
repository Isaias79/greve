from django.db import models


#class Produto extends models.Model{}
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    
    #public static void main
    def __str__(self): # Metodo que recebe um objeto que converte automaticamente para string
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)

    def __str__(self):
        return self.nome
    
'''
public class Produto extends models.Model {
    String nome;
    float preco;
    public String toString() {
        String nome = 'Sr. João'
        this.nome = nome
        return nome;
    }
}
'''
    #quantidade = 

# COLOCAR FLOAT DA PROBLEMA NA PROGAMAÇÃO
# Create your models here.
