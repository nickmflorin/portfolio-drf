from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers


router = routers.DefaultRouter()

urlpatterns = [
    path('admin_tools/', include('admin_tools.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include([
        path('experience/', include('portfolio.app.experience.urls')),
        path('education/', include('portfolio.app.education.urls')),
        path('skills/', include('portfolio.app.skills.urls')),
        path('projects/', include('portfolio.app.projects.urls')),
        path('courses/', include('portfolio.app.courses.urls')),
        path('schools/', include('portfolio.app.schools.urls')),
        path('companies/', include('portfolio.app.companies.urls')),
    ])),
]

if settings.DEBUG:
    # TODO: Figure out how to serve static files when DEBUG != True.
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = "Personal Portfolio Admin"
admin.site.site_title = "Nick Florin"
admin.site.index_title = "Portfolio Portal"
