from rest_framework import serializers

from portfolio.app.education.models import Education

from portfolio.app.common.serializers import PortfolioSerializer
from portfolio.app.skills.serializers import NestedSkillSerializer

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


class NestedProjectSerializer(PortfolioSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    showcase = serializers.BooleanField()

    class Meta:
        model = Project
        fields = PortfolioSerializer.Meta.fields + (
            'name', 'description', 'showcase')


class ListProjectSerializer(NestedProjectSerializer):

    class Meta:
        model = Project
        fields = NestedProjectSerializer.Meta.fields


class DetailProjectSerializer(ListProjectSerializer):
    skills = NestedSkillSerializer(many=True)
    files = ProjectFileSerializer(many=True)
    showcase_description = serializers.CharField()

    class Meta:
        model = Project
        fields = ListProjectSerializer.Meta.fields + (
            'skills', 'files', 'showcase_description')

    def to_representation(self, instance):
        from portfolio.app.education.serializers import NestedEducationSerializer
        from portfolio.app.experience.serializers import NestedExperienceSerializer

        data = super(DetailProjectSerializer, self).to_representation(instance)
        if isinstance(instance.content_object, Education):
            data['education'] = NestedEducationSerializer(
                instance.content_object).data
        else:
            data['experience'] = NestedExperienceSerializer(
                instance.content_object).data
        return data
