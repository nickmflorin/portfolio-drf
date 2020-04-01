from rest_framework import serializers
from portfolio.app.common.serializers import PortfolioSerializer

from .models import Comment


class CommentSerializer(PortfolioSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    email = serializers.CharField()
    value = serializers.CharField()
    public = serializers.BooleanField()

    class Meta:
        model = Comment
        fields = PortfolioSerializer.Meta.fields + (
            'name', 'email', 'value', 'public')
