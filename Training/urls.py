from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from base.views import Index


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('produtos/', include('products.urls')),
    path('clientes/', include('customer.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

