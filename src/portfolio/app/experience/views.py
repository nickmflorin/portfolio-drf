from rest_framework import viewsets

from .models import Experience
from .serializers import ExperienceSerializer


class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
