from rest_framework import viewsets

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    # TODO: Allow filtering by the education, or allow a /courses/<school>
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
