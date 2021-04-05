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
