from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('experience/', include('portfolio.app.experience.urls')),
        path('education/', include('portfolio.app.education.urls')),
        path('skills/', include('portfolio.app.skills.urls')),
    ])),
]

# This is only active when DEBUG=True  # noqa
# TODO: Figure out how to serve static files when DEBUG != True.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
