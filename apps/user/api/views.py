from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from apps.user.api.serializers import (UserSerializer)
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAuthenticated,)