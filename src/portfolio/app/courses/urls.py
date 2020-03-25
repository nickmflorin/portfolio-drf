from rest_framework import routers

from .views import CourseViewSet


app_name = 'courses'

router = routers.SimpleRouter()
router.register('', CourseViewSet)
urlpatterns = router.urls
