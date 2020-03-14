from rest_framework import viewsets

from .models import Education
from .serializers import EducationSerializer


class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer
