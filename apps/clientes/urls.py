from django.urls import include, path

from . import views

app_name = 'clientes'

urlpatterns = [
    path('api/', include('apps.clientes.api.urls')),
]