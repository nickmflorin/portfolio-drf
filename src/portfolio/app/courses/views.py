from rest_framework import viewsets

from portfolio.app.common.views import PartitionedViewSetMixin

from .models import Course
from .serializers import DetailCourseSerializer, ListCourseSerializer


class CourseViewSet(PartitionedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    # TODO: Allow filtering by the education, or allow a /courses/<school>
    queryset = Course.objects.all()
    detail_serializer_class = DetailCourseSerializer
    list_serializer_class = ListCourseSerializer
