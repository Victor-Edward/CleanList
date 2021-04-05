from django import forms
from .models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'product_type', 'brand', 'quantity', 'photo')

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = "Nome"
        self.fields['product_type'].label = "Tipo de produto"
        self.fields['brand'].label = "Marca"
        self.fields['quantity'].label = "Quantidade em estoque"
        self.fields['photo'].label = "Foto"

