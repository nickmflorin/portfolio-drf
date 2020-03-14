from django.contrib import admin
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('experience/', include('portfolio.app.experience.urls')),
        path('education/', include('portfolio.app.education.urls')),
    ])),
]
