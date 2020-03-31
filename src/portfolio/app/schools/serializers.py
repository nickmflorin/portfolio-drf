from rest_framework import serializers

from portfolio.app.common.serializers import PortfolioSerializer
from .models import School


class BasicSchoolSerializer(PortfolioSerializer):

    class Meta:
        model = School
        fields = PortfolioSerializer.Meta.fields


class SchoolSerializer(PortfolioSerializer):
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    logo = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = School
        fields = PortfolioSerializer.Meta.fields + (
            'name', 'city', 'state', 'logo', 'description')
        collapsed = BasicSchoolSerializer
