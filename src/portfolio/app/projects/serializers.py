from rest_framework import serializers
from .models import Project


class BasicProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')


class ProjectSerializer(BasicProjectSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Project
        # TODO: We want to reference the education and projects that are in here.
        fields = BasicProjectSerializer.Meta.fields + ()
