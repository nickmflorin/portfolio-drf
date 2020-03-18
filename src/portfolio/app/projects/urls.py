from rest_framework import routers

from .views import ProjectViewSet


app_name = 'projects'

router = routers.SimpleRouter()
router.register('', ProjectViewSet)
urlpatterns = router.urls
