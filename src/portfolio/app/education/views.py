from rest_framework import viewsets

from portfolio.app.common.views import PartitionedViewSetMixin

from .models import Education
from .serializers import DetailEducationSerializer, ListEducationSerializer


class EducationViewSet(PartitionedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    list_serializer_class = ListEducationSerializer
    detail_serializer_class = DetailEducationSerializer
    queryset = Education.objects.all()
