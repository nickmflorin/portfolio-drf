from portfolio.app.common.views import PartitionedReadOnlyViewSet

from .models import Education
from .serializers import DetailEducationSerializer, ListEducationSerializer


class EducationViewSet(PartitionedReadOnlyViewSet):
    queryset = Education.objects.all()
    list_serializer_class = ListEducationSerializer
    detail_serializer_class = DetailEducationSerializer
