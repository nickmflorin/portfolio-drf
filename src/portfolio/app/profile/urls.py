from django.urls import path

from .views import ProfileViewSet


app_name = 'profile'

urlpatterns = [
    path('', ProfileViewSet.as_view({
        'get': 'retrieve',
    })),
]
