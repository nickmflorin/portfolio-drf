from rest_framework import serializers

from portfolio.app.projects.serializers import BasicProjectSerializer
from portfolio.app.common.serializers import HorizonSerializer
from portfolio.app.schools.serializers import SchoolSerializer
from portfolio.app.skills.serializers import SkillSerializer

from .models import Education


class EducationSerializer(HorizonSerializer):
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
        extended_fields = {
            'projects': (BasicProjectSerializer, {'many': True}),
            'courses': serializers.SerializerMethodField,
            'skills': (SkillSerializer, {'many': True}),
        }

    def get_courses(self, instance):
        # This has to be in a serializer method field instead of just simply doing
        # >>> EducationSerializer()
        # >>>   courses = BasicCourseSerializer(many=True)
        # because this would introduce a circular import.
        from portfolio.app.courses.serializers import BasicCourseSerializer
        return BasicCourseSerializer(instance.courses.all(), many=True).data
