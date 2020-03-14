from django.urls import path

from .views import EducationViewSet


app_name = 'education'

urlpatterns = [
    path('', EducationViewSet.as_view({
        'get': 'list',
    })),
]
