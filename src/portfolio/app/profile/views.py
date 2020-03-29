from rest_framework import viewsets

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.first()
    serializer_class = ProfileSerializer
