from rest_framework import routers

from .views import ResumeViewSet


app_name = 'resume'

router = routers.SimpleRouter()
router.register('', ResumeViewSet, basename='resume')
urlpatterns = router.urls
