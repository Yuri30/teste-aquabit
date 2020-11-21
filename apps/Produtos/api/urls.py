from rest_framework import routers
from django.urls import include, path
from apps.Produtos.api.views import ProdutosViewSet, PratosViewSet

router = routers.DefaultRouter()

router.register('produtos', ProdutosViewSet, basename = 'produtos')
router.register('pratos', PratosViewSet, basename = 'pratos')


urlpatterns = router.urls