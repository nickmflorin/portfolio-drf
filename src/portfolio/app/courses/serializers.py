from rest_framework import serializers

from portfolio.app.common.serializers import PortfolioSerializer
from portfolio.app.education.serializers import EducationSerializer
from portfolio.app.skills.serializers import BasicSkillSerializer

from .models import Course


class BasicCourseSerializer(PortfolioSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Course
        fields = PortfolioSerializer.Meta.fields + ('name', 'description')


class CourseSerializer(BasicCourseSerializer):
    education = EducationSerializer()
    skills = BasicSkillSerializer(many=True)

    class Meta:
        model = Course
        fields = BasicCourseSerializer.Meta.fields + ('education', 'skills')
