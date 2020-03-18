from rest_framework import serializers
from .models import School, Education


class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    logo = serializers.ImageField()
    description = serializers.CharField()

    class Meta:
        model = School
        fields = ('id', 'name', 'city', 'state', 'logo', 'description')


class EducationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    school = SchoolSerializer()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    degree = serializers.CharField()
    major = serializers.CharField()
    minor = serializers.CharField()
    concentration = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Education
        fields = (
            'id', 'school', 'start_date', 'end_date', 'degree', 'major', 'minor',
            'concentration', 'description')
