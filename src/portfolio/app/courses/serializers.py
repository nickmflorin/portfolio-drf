from rest_framework import serializers

from portfolio.app.common.serializers import PortfolioSerializer
from portfolio.app.education.serializers import NestedEducationSerializer
from portfolio.app.skills.serializers import NestedSkillSerializer

from .models import Course


class NestedCourseSerializer(PortfolioSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Course
        fields = PortfolioSerializer.Meta.fields + ('name', 'description')


class ListCourseSerializer(NestedCourseSerializer):

    class Meta:
        model = Course
        fields = NestedCourseSerializer.Meta.fields


class DetailCourseSerializer(ListCourseSerializer):
    education = NestedEducationSerializer()
    skills = NestedSkillSerializer(many=True)

    class Meta:
        model = Course
        fields = ListCourseSerializer.Meta.fields + ('education', 'skills')
