from rest_framework import serializers

from portfolio.app.projects.serializers import ProjectSerializer
from portfolio.app.skills.serializers import SkillSerializer

from .models import Experience, Company


class CompanySerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    logo = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = Company
        fields = ('id', 'name', 'city', 'state', 'logo', 'description')


class ExperienceSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    company = CompanySerializer()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    title = serializers.CharField()
    description = serializers.CharField()
    current = serializers.BooleanField()
    projects = ProjectSerializer(many=True)
    skills = SkillSerializer(many=True)

    class Meta:
        model = Experience
        fields = ('id', 'company', 'start_date', 'end_date', 'title',
            'description', 'projects', 'skills')
