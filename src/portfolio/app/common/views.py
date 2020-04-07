from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from abc import ABCMeta, abstractproperty


class PartitionedViewSetMixin(metaclass=ABCMeta):
    """
    Abstract parent viewset for cases where we have different serializers for
    list and detail endpoints.
    """
    @abstractproperty
    def queryset(self):
        pass

    def get_serializer_class(self):
        if self.action == 'list':
            return self.list_serializer_class
        return self.detail_serializer_class

    @abstractproperty
    def detail_serializer_class(self):
        pass

    @abstractproperty
    def list_serializer_class(self):
        pass

    def get_object(self):
        filter = {}
        filter[self.lookup_field] = self.kwargs[self.lookup_field]
        obj = get_object_or_404(self.get_queryset(), **filter)
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request):
        serializer_cls = self.get_serializer_class()
        serializer = serializer_cls(self.get_queryset(), many=True,
            context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_object()
        serializer_cls = self.get_serializer_class()
        serializer = serializer_cls(obj, context={'request': request})
        return Response(serializer.data)
