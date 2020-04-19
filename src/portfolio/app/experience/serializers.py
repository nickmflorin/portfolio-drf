from rest_framework import serializers

from portfolio.app.common.serializers import HorizonSerializer
from portfolio.app.companies.serializers import CompanySerializer
from portfolio.app.projects.serializers import NestedProjectSerializer
from portfolio.app.skills.serializers import NestedSkillSerializer

from .models import Experience


class NestedExperienceSerializer(HorizonSerializer):
    company = CompanySerializer()
    title = serializers.CharField()
    short_title = serializers.CharField()
    description = serializers.CharField()
    current = serializers.BooleanField()
    include_in_resume = serializers.BooleanField()

    class Meta:
        model = Experience
        fields = HorizonSerializer.Meta.fields + (
            'company', 'title', 'description', 'current', 'short_title',
            'include_in_resume')


class ListExperienceSerializer(NestedExperienceSerializer):

    class Meta:
        model = Experience
        fields = NestedExperienceSerializer.Meta.fields


class DetailExperienceSerializer(ListExperienceSerializer):
    projects = NestedProjectSerializer(many=True)
    skills = NestedSkillSerializer(many=True)

    class Meta:
        model = Experience
        fields = ListExperienceSerializer.Meta.fields + ('projects', 'skills')
