from rest_framework import serializers
from portfolio.app.common.serializers import PortfolioSerializer

from .models import Comment


class CommentSerializer(PortfolioSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    email = serializers.CharField()
    comment = serializers.CharField()
    public = serializers.BooleanField()

    class Meta:
        model = Comment
        fields = PortfolioSerializer.Meta.fields + (
            'name', 'email', 'comment', 'public')

    def validate(self, data):
        if data['public'] is False:
            if not data['email']:
                raise serializers.ValidationError(
                    "Email must be provided for non-public comments.")
        return data
