from portfolio.app.common.views import PartitionedReadOnlyViewSet

from .models import Project
from .serializers import DetailProjectSerializer, ListProjectSerializer


class ProjectViewSet(PartitionedReadOnlyViewSet):
    queryset = Project.objects.all()
    detail_serializer_class = DetailProjectSerializer
    list_serializer_class = ListProjectSerializer
