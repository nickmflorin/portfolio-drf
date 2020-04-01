from portfolio.app.common.views import PartitionedReadOnlyViewSet

from .models import Experience
from .serializers import DetailExperienceSerializer, ListExperienceSerializer


class ExperienceViewSet(PartitionedReadOnlyViewSet):
    queryset = Experience.objects.all()
    detail_serializer_class = DetailExperienceSerializer
    list_serializer_class = ListExperienceSerializer
