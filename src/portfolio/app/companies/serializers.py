from rest_framework import serializers
from portfolio.app.common.serializers import PortfolioSerializer

from .models import Company


class CompanySerializer(PortfolioSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    url = serializers.URLField()
    logo = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = Company
        fields = PortfolioSerializer.Meta.fields + (
            'id', 'name', 'city', 'state', 'url', 'logo', 'description')
