from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=150, default='')

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=120, default='')
    product_type = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    quantity = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
    

    

    