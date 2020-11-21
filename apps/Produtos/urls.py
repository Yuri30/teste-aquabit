from django.urls import include, path

from . import views

app_name = 'Produtos'

urlpatterns = [
    path('api/', include('apps.Produtos.api.urls')),
]