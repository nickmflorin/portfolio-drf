from rest_framework import routers

from .views import CompanyViewSet


app_name = 'companies'

router = routers.SimpleRouter()
router.register('', CompanyViewSet)
urlpatterns = router.urls
