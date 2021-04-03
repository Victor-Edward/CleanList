from django.urls import path
from basic_app.views import (Index, ProductDetailView, CreateProductView,
                            ProductListView, ProductUpdateView, ProductDeleteview,)

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('products/', ProductListView.as_view(), name='product_view'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/novo/', CreateProductView.as_view(), name='product_create'),
    path('poducts/<int:pk>/editar', ProductUpdateView.as_view(), name='product_edit'),
    path('products/<int:pk>/deletar', ProductDeleteview.as_view(), name='product_delete'),
]
