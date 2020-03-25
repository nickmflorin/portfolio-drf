from rest_framework import viewsets

from .models import School
from .serializers import SchoolSerializer


class SchoolViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
