from rest_framework import serializers

from portfolio.app.common.serializers import HorizonSerializer
from portfolio.app.companies.serializers import CompanySerializer

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
    projects = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Experience
        fields = BasicExperienceSerializer.Meta.fields + ('projects', 'skills')

    def get_projects(self, instance):
        from portfolio.app.projects.serializers import BasicProjectSerializer
        qs = instance.projects.all()
        return BasicProjectSerializer(qs, many=True).data

    def get_skills(self, instance):
        from portfolio.app.skills.serializers import BasicSkillSerializer
        qs = instance.skill_set.all()
        return BasicSkillSerializer(qs, many=True).data
