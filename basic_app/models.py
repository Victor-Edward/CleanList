from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=150)


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    quantity = models.IntegerField()


    