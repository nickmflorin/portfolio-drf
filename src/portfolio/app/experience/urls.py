from rest_framework import routers

from .views import ExperienceViewSet


app_name = 'experience'

router = routers.SimpleRouter()
router.register('', ExperienceViewSet)
urlpatterns = router.urls
