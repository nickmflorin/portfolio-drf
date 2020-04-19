from rest_framework import serializers

from portfolio.app.projects.serializers import NestedProjectSerializer
from portfolio.app.common.serializers import HorizonSerializer
from portfolio.app.schools.serializers import SchoolSerializer
from portfolio.app.skills.serializers import NestedSkillSerializer

from .models import Education


class NestedEducationSerializer(HorizonSerializer):
    school = SchoolSerializer()
    degree = serializers.CharField()
    major = serializers.CharField()
    gpa = serializers.FloatField()
    minor = serializers.CharField()
    concentration = serializers.CharField()
    description = serializers.CharField()
    include_in_resume = serializers.BooleanField()

    class Meta:
        model = Education
        fields = HorizonSerializer.Meta.fields + (
            'id', 'school', 'degree', 'major', 'minor', 'concentration',
            'description', 'gpa', 'include_in_resume')


class ListEducationSerializer(NestedEducationSerializer):

    class Meta:
        model = Education
        fields = NestedEducationSerializer.Meta.fields


class DetailEducationSerializer(ListEducationSerializer):
    projects = NestedProjectSerializer(many=True)
    skills = NestedSkillSerializer(many=True)
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = NestedEducationSerializer.Meta.fields + (
            'projects', 'skills', 'courses')

    def get_courses(self, instance):
        from portfolio.app.courses.serializers import NestedCourseSerializer
        return NestedCourseSerializer(instance.courses.all(), many=True).data
