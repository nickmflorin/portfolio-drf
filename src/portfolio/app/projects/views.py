from rest_framework import viewsets

from portfolio.app.common.views import PartitionedViewSetMixin

from .models import Project
from .serializers import DetailProjectSerializer, ListProjectSerializer


class ProjectViewSet(PartitionedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    detail_serializer_class = DetailProjectSerializer
    list_serializer_class = ListProjectSerializer
