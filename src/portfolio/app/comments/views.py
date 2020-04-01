from rest_framework import viewsets, mixins

from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
        mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.filter(public=True).all()
