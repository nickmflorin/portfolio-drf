from rest_framework import serializers

from portfolio.app.common.serializers import PortfolioSerializer
from portfolio.app.skills.serializers import BasicSkillSerializer

from .models import Project


class ProjectFileSerializer(PortfolioSerializer):
    file = serializers.FileField()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Project
        fields = PortfolioSerializer.Meta.fields + ('file', 'name', 'description')


class BasicProjectSerializer(PortfolioSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Project
        fields = PortfolioSerializer.Meta.fields + ('name', 'description')


class ProjectSerializer(BasicProjectSerializer):
    skills = BasicSkillSerializer(many=True)
    files = ProjectFileSerializer(many=True)

    class Meta:
        model = Project
        fields = BasicProjectSerializer.Meta.fields + ('skills', 'files', )
