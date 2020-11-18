from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.clientes.api.serializers import (ClienteSerializer)
from apps.clientes.models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = (IsAdminUser, IsAuthenticated,)