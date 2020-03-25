from rest_framework import routers

from .views import SchoolViewSet


app_name = 'schools'

router = routers.SimpleRouter()
router.register('', SchoolViewSet)
urlpatterns = router.urls
