from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description')
