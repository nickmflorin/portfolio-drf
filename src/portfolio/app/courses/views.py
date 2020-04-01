from portfolio.app.common.views import PartitionedReadOnlyViewSet

from .models import Course
from .serializers import DetailCourseSerializer, ListCourseSerializer


class CourseViewSet(PartitionedReadOnlyViewSet):
    # TODO: Allow filtering by the education, or allow a /courses/<school>
    queryset = Course.objects.all()
    detail_serializer_class = DetailCourseSerializer
    list_serializer_class = ListCourseSerializer
