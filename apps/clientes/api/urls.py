from rest_framework import routers
from django.urls import include, path
from apps.clientes.api.views import ClienteViewSet

router = routers.DefaultRouter()

router.register('clientes', ClienteViewSet, basename = 'clientes')

urlpatterns = router.urls