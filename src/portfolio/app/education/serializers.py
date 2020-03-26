from rest_framework import serializers

from portfolio.app.common.serializers import HorizonSerializer
from portfolio.app.schools.serializers import SchoolSerializer

from .models import Education


class BasicEducationSerializer(HorizonSerializer):
    school = SchoolSerializer()
    degree = serializers.CharField()
    major = serializers.CharField()
    gpa = serializers.FloatField()
    minor = serializers.CharField()
    concentration = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Education
        fields = HorizonSerializer.Meta.fields + (
            'id', 'school', 'degree', 'major', 'minor', 'concentration',
            'description', 'gpa')


class EducationSerializer(BasicEducationSerializer):
    projects = serializers.SerializerMethodField()
    skills = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = BasicEducationSerializer.Meta.fields + (
            'projects', 'skills', 'courses')

    def get_courses(self, instance):
        from portfolio.app.courses.serializers import BasicCourseSerializer
        courses = instance.course_set.all()
        return BasicCourseSerializer(courses, many=True).data

    def get_projects(self, instance):
        from portfolio.app.projects.serializers import BasicProjectSerializer
        qs = instance.projects.all()
        return BasicProjectSerializer(qs, many=True).data

    def get_skills(self, instance):
        from portfolio.app.skills.serializers import BasicSkillSerializer
        qs = instance.skill_set.all()
        return BasicSkillSerializer(qs, many=True).data
