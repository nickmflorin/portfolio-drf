from rest_framework import routers

from .views import EducationViewSet


app_name = 'education'

router = routers.SimpleRouter()
router.register('', EducationViewSet, basename='education')
urlpatterns = router.urls
