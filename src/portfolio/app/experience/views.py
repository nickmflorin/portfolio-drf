from rest_framework import viewsets

from portfolio.app.common.views import PartitionedViewSetMixin

from .models import Experience
from .serializers import DetailExperienceSerializer, ListExperienceSerializer


class ExperienceViewSet(PartitionedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    detail_serializer_class = DetailExperienceSerializer
    list_serializer_class = ListExperienceSerializer
