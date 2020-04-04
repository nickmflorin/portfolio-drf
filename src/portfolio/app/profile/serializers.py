from rest_framework import serializers

from portfolio.app.common.serializers import PortfolioSerializer
from .models import Profile


class ProfileSerializer(PortfolioSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    middle_name = serializers.CharField()
    email = serializers.EmailField()
    github_url = serializers.URLField()
    linkedin_url = serializers.URLField()
    resume = serializers.FileField()
    intro = serializers.CharField()
    headshot = serializers.ImageField()

    class Meta:
        model = Profile
        fields = PortfolioSerializer.Meta.fields + (
            'first_name', 'last_name', 'middle_name', 'email', 'github_url',
            'linkedin_url', 'resume', 'intro', 'headshot')
