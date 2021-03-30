from django.db import models

class Customer(models.Model):
    nome = models.CharField(max_length=100)
    contato = models.CharField(max_length=100)
    endereço = models.CharField(max_length=150, default='')
    


class Product(models.Model):
    nome = models.CharField(max_length=100)
    tipo_de_produto = models.CharField(max_length=100)
    quantitade = models.IntegerField()
    


    