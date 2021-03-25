from django.urls import path
from basic_app.views import Index

urlpatterns = [
    path('', Index.as_view(), name='index'),
]
