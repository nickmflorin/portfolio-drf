from rest_framework import routers

from .views import CommentViewSet


app_name = 'comments'

router = routers.SimpleRouter()
router.register('', CommentViewSet, basename='comments')
urlpatterns = router.urls
