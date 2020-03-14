from rest_framework import serializers
from .models import Experience, Company


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'city', 'state')


class ExperienceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    company = CompanySerializer()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    class Meta:
        model = Experience
        fields = ('id', 'company', 'start_date', 'end_date')
