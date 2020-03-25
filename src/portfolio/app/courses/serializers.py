from rest_framework import serializers

from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'description')
