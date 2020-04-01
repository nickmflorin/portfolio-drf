from rest_framework import serializers
from .models import Skill


class NestedSkillSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    class Meta:
        model = Skill
        fields = ('id', 'name')


class ListSkillSerializer(NestedSkillSerializer):

    class Meta:
        model = Skill
        fields = NestedSkillSerializer.Meta.fields


class DetailSkillSerializer(ListSkillSerializer):
    educations = serializers.SerializerMethodField()
    courses = serializers.SerializerMethodField()
    experiences = serializers.SerializerMethodField()
    projects = serializers.SerializerMethodField()

    class Meta:
        model = Skill
        fields = ListSkillSerializer.Meta.fields + (
            'educations', 'courses', 'experiences', 'projects')

    def get_educations(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since EducationSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.education.serializers import NestedEducationSerializer
        return NestedEducationSerializer(instance.educations.all(), many=True).data

    def get_courses(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since CourseSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.courses.serializers import NestedCourseSerializer
        return NestedCourseSerializer(instance.courses.all(), many=True).data

    def get_experiences(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since ExperienceSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.experience.serializers import NestedExperienceSerializer
        return NestedExperienceSerializer(instance.experiences.all(), many=True).data

    def get_projects(self, instance):
        # These must be written as SerializerMethodField(s) in order to avoid
        # circular imports, since ExperienceSerializer also uses the
        # BasicSkillSerializer.
        from portfolio.app.projects.serializers import NestedProjectSerializer
        return NestedProjectSerializer(instance.projects.all(), many=True).data
