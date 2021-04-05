from django.urls import path
from products.views import (ProductDetailView, CreateProductView,
                            ProductListView, ProductUpdateView, ProductDeleteview)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_view'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('novo/', CreateProductView.as_view(), name='product_create'),
    path('<int:pk>/editar', ProductUpdateView.as_view(), name='product_edit'),
    path('<int:pk>/deletar', ProductDeleteview.as_view(), name='product_delete'),
]
