from rest_framework import viewsets, mixins
from rest_framework.permissions import BasePermission, AllowAny, SAFE_METHODS

from .models import Comment
from .serializers import CommentSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
        mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny | ReadOnly]
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(public=True).all()
