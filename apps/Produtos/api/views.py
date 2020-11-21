from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.Produtos.api.serializers import (ProdutosSerializer, PratosSerializer)
from apps.Produtos.models import Produtos, Pratos


class ProdutosViewSet(viewsets.ModelViewSet):
    queryset = Produtos.objects.all()
    serializer_class = ProdutosSerializer
    permission_classes = (IsAdminUser, IsAuthenticated,)

class PratosViewSet(viewsets.ModelViewSet):
    queryset = Pratos.objects.all()
    serializer_class = PratosSerializer
    permission_classes = (IsAdminUser, IsAuthenticated,)    