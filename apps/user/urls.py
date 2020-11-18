from django.urls import include, path

from . import views

app_name = 'user'

urlpatterns = [
    path('api/', include('apps.user.api.urls')),
]