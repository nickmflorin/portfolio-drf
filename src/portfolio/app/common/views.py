from django.shortcuts import get_object_or_404
''
from rest_framework import viewsets
from rest_framework.response import Response

from abc import ABCMeta, abstractproperty


class PartitionedReadOnlyViewSet(viewsets.ReadOnlyModelViewSet, metaclass=ABCMeta):
    """
    Abstract parent viewset for cases where we have different serializers for
    list and detail endpoints.
    """
    @abstractproperty
    def queryset(self):
        pass

    @abstractproperty
    def detail_serializer_class(self):
        pass

    @abstractproperty
    def list_serializer_class(self):
        pass

    def list(self, request):
        serializer = self.list_serializer_class(self.queryset, many=True,
            context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.detail_serializer_class(obj, context={'request': request})
        return Response(serializer.data)
