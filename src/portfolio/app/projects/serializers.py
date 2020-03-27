from rest_framework import serializers

from portfolio.app.skills.serializers import BasicSkillSerializer

from .models import Project


class BasicProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')


class ProjectSerializer(BasicProjectSerializer):
    skills = BasicSkillSerializer(many=True)

    class Meta:
        model = Project
        fields = BasicProjectSerializer.Meta.fields + ('skills', )
