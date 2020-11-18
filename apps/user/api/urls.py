from rest_framework import routers
from django.urls import include, path
from apps.user.api.views import UserViewSet

router = routers.DefaultRouter()

router.register('user', UserViewSet, basename = 'user')

urlpatterns = router.urls