from rest_framework import serializers
from .models import Skill


class BasicSkillSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    class Meta:
        model = Skill
        fields = ('id', 'name')


class SkillSerializer(BasicSkillSerializer):
    educations = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()
    experiences = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = BasicSkillSerializer.Meta.fields + (
            'educations', 'courses', 'experiences')

    def get_educations(self, instance):
        from portfolio.app.education.serializers import BasicEducationSerializer
        return BasicEducationSerializer(instance.educations.all(), many=True).data

    def get_courses(self, instance):
        from portfolio.app.courses.serializers import BasicCourseSerializer
        return BasicCourseSerializer(instance.courses.all(), many=True).data

    def get_experiences(self, instance):
        from portfolio.app.experience.serializers import BasicExperienceSerializer
        return BasicExperienceSerializer(instance.experiences.all(), many=True).data
