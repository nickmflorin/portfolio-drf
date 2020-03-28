from rest_framework import serializers

from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    url = serializers.URLField()
    logo = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'city', 'state', 'url', 'logo', 'description')
