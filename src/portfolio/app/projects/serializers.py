from rest_framework import serializers

from portfolio.app.education.models import Education

from portfolio.app.common.serializers import PortfolioSerializer
from portfolio.app.skills.serializers import BasicSkillSerializer

from .models import Project


class ProjectFileSerializer(PortfolioSerializer):
    file = serializers.FileField()
    name = serializers.CharField()
    description = serializers.CharField()
    caption = serializers.CharField()

    class Meta:
        model = Project
        fields = PortfolioSerializer.Meta.fields + (
            'file', 'name', 'description', 'caption')


class BasicProjectSerializer(PortfolioSerializer):
    name = serializers.CharField()
    short_description = serializers.CharField()
    showcase = serializers.BooleanField()

    class Meta:
        model = Project
        fields = PortfolioSerializer.Meta.fields + (
            'name', 'short_description', 'showcase')


class ProjectSerializer(BasicProjectSerializer):
    skills = BasicSkillSerializer(many=True)
    files = ProjectFileSerializer(many=True)
    long_description = serializers.CharField()

    class Meta:
        model = Project
        fields = BasicProjectSerializer.Meta.fields + (
            'skills', 'files', 'long_description')

    def to_representation(self, instance):
        from portfolio.app.education.serializers import EducationSerializer
        from portfolio.app.experience.serializers import BasicExperienceSerializer

        data = super(ProjectSerializer, self).to_representation(instance)
        if isinstance(instance.content_object, Education):
            data['education'] = EducationSerializer(
                instance.content_object, context={'collapsed': True}).data
        else:
            data['experience'] = BasicExperienceSerializer(instance.content_object).data
        return data
