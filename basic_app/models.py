from django.db import models
from django.urls import reverse

class Customer(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=150, default='')
    photo = models.ImageField(upload_to='customers/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("customer_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=120, default='')
    product_type = models.CharField(max_length=100, default='')
    brand = models.CharField(max_length=100, default='')
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
    
    

    

    