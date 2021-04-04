from django.urls import path
from basic_app.views import (Index, ProductDetailView, CreateProductView,
                            ProductListView, ProductUpdateView, ProductDeleteview,
                            CustomerListView, CustomerDetailView, CustomerDeleteView,
                            CreateCustomerView, CustomerUpdateView)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='product_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/novo/', CreateProductView.as_view(), name='product_create'),
    path('poducts/<int:pk>/editar', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/deletar', ProductDeleteview.as_view(), name='product_delete'),

    path('clientes/', CustomerListView.as_view(), name='customer_view'),
    path('clientes/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('clientes/novo/', CreateCustomerView.as_view(), name='customer_create'),
    path('clientes/<int:pk>/editar', CustomerUpdateView.as_view(), name='customer_edit'),
    path('clientes/<int:pk>/deletar', CustomerDeleteView.as_view(), name='customer_delete'),   
]
