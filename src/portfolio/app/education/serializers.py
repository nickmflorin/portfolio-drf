from rest_framework import serializers

from portfolio.app.projects.serializers import ProjectSerializer
from portfolio.app.skills.serializers import SkillSerializer

from .models import School, Education, Course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description')


class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    logo = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = School
        fields = ('id', 'name', 'city', 'state', 'logo', 'description')


class EducationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    school = SchoolSerializer()
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    degree = serializers.CharField()
    major = serializers.CharField()
    gpa = serializers.FloatField()
    minor = serializers.CharField()
    concentration = serializers.CharField()
    description = serializers.CharField()
    ongoing = serializers.BooleanField()
    projects = ProjectSerializer(many=True)
    skills = SkillSerializer(many=True)
    courses = CourseSerializer(many=True)

    class Meta:
        model = Education
        fields = (
            'id', 'school', 'start_date', 'end_date', 'degree', 'major', 'minor',
            'concentration', 'description', 'projects', 'gpa', 'skills',
            'courses')
