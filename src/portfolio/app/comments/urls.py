from rest_framework import routers

from .views import CommentViewSet


app_name = 'comments'

router = routers.SimpleRouter()
router.register('', CommentViewSet)
urlpatterns = router.urls
