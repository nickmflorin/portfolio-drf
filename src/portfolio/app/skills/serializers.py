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
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = BasicSkillSerializer.Meta.fields + (
            'educations', 'courses', 'experiences', 'projects')
        collapsed = BasicSkillSerializer

    def get_educations(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since EducationSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.education.serializers import BasicEducationSerializer
        return BasicEducationSerializer(instance.educations.all(), many=True).data

    def get_courses(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since CourseSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.courses.serializers import BasicCourseSerializer
        return BasicCourseSerializer(instance.courses.all(), many=True).data

    def get_experiences(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since ExperienceSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.experience.serializers import BasicExperienceSerializer
        return BasicExperienceSerializer(instance.experiences.all(), many=True).data

    def get_projects(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since ExperienceSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.projects.serializers import BasicProjectSerializer
        return BasicProjectSerializer(instance.projects.all(), many=True).data
