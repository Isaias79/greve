from django.db import models


#class Produto extends models.Model{}
class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    quantidade = models.IntegerField(default=0)
    ## 1 Para Muitos (1:N)
    ## Se colocar no fornecedor vai mudar o (N) --> Poderia ficar no caso (N,1)
    fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE, default=0, related_name='produto')

class Produto_One(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    quantidade = models.IntegerField(default=0)
    ## 1 Para Muitos (N:N)
    ## Se colocar no fornecedor vai mudar o (N)
    fornecedor = models.ManyToManyField('Fornecedor')

class Produto_One_to_One(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    quantidade = models.IntegerField(default=0)
    ## 1 Para Muitos (1:1)
    ## Se colocar no fornecedor vai mudar o (N)
    fornecedor = models.OneToOneField('Fornecedor', on_delete=models.CASCADE, default=0)
'''
### FUNCIONA #####
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    quantidade = models.IntegerField(default=0) #balnk=True, null=True
    
    #public static void main
    def __str__(self): # Metodo que recebe um objeto que converte automaticamente para string
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)

    def __str__(self):
        return self.nome



class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.Requerente
        
class Produto(models.Model):
    nome = models.CharField()
    preco = models.IntegerField()
    quantidade = models.IntegerField(default=0)
    ## 1 Para Muitos (1:N)
    
    def __str__(self):
        return self.Requerente
'''
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
