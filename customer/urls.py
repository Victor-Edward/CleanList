from django.urls import path
from customer.views import (CustomerListView, CustomerDetailView, CustomerDeleteView,
                            CreateCustomerView, CustomerUpdateView)

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_view'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('novo/', CreateCustomerView.as_view(), name='customer_create'),
    path('<int:pk>/editar', CustomerUpdateView.as_view(), name='customer_edit'),
    path('<int:pk>/deletar', CustomerDeleteView.as_view(), name='customer_delete'),   
]
