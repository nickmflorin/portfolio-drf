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
        errors = {}
        if data['public'] is False and not data['email']:
            errors['email'] = "Email must be provided for non-public comments."
            raise serializers.ValidationError(errors)
        return data
