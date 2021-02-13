from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from alojamiento.views import index, reservas


urlpatterns = [
    path('', index, name='index'),
    path('reservas/', reservas, name='reservas')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
