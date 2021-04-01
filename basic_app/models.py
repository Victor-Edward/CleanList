from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=150, default='')
    
class Product(models.Model):
    name = models.CharField(max_length=120, default='')
    product_type = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    quantity = models.IntegerField(default=0)
    

    

    