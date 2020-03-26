from rest_framework import serializers

from portfolio.app.common.serializers import PortfolioSerializer
from portfolio.app.education.serializers import BasicEducationSerializer
from .models import Course


class BasicCourseSerializer(PortfolioSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Course
        fields = PortfolioSerializer.Meta.fields + ('name', 'description')


class CourseSerializer(BasicCourseSerializer):
    education = BasicEducationSerializer()

    class Meta:
        model = Course
        fields = BasicCourseSerializer.Meta.fields + ('education', )
