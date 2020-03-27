from rest_framework import serializers

from portfolio.app.common.serializers import HorizonSerializer
from portfolio.app.companies.serializers import CompanySerializer
from portfolio.app.projects.serializers import BasicProjectSerializer
from portfolio.app.skills.serializers import BasicSkillSerializer

from .models import Experience


class BasicExperienceSerializer(HorizonSerializer):
    company = CompanySerializer()
    title = serializers.CharField()
    description = serializers.CharField()
    current = serializers.BooleanField()

    class Meta:
        model = Experience
        fields = HorizonSerializer.Meta.fields + (
            'company', 'title', 'description', 'current')


class ExperienceSerializer(BasicExperienceSerializer):
    projects = BasicProjectSerializer(many=True)
    skills = BasicSkillSerializer(many=True)

    class Meta:
        model = Experience
        fields = BasicExperienceSerializer.Meta.fields + ('projects', 'skills')
