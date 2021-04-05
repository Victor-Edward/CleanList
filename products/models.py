from django.db import models
from django.urls import reverse

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