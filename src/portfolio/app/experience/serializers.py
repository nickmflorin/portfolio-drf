from rest_framework import serializers
from .models import Experience, Company


class CompanySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()

    class Meta:
        model = Company
        fields = ('__all__', )


class ExperienceSerializer(serializers.Serializer):
    company = CompanySerializer()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()

    class Meta:
        model = Experience
        fields = ('__all__', )
