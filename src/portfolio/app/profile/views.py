from rest_framework import viewsets, mixins
from rest_framework.exceptions import APIException  # noqa
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Profile.objects.first()
    serializer_class = ProfileSerializer

    def get_object(self):
        if Profile.objects.count() != 1:
            # This is temporary, at least for now.  We should maybe raise an
            # exception that is handled by DRF.
            raise Exception("There should only ever be one profile.")
        return Profile.objects.first()

    def retrieve(self, *args):
        obj = self.get_object()
        # We have to pass in the request context so the absolute url can be
        # used.
        data = self.serializer_class(obj, context={'request': self.request}).data
        return Response(data)
