from rest_framework import routers

from .views import EducationViewSet


app_name = 'education'

router = routers.SimpleRouter()
router.register('', EducationViewSet)
urlpatterns = router.urls
