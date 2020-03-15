from rest_framework import serializers
from .models import Skill


class SkillSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()

    class Meta:
        model = Skill
        fields = ('id', 'name')
