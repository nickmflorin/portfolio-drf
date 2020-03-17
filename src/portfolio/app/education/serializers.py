from rest_framework import serializers
from .models import School, Education


class SchoolSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()
    logo = serializers.ImageField()

    class Meta:
        model = School
        fields = ('id', 'name', 'city', 'state', 'logo')


class EducationSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    school = SchoolSerializer()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
    degree = serializers.CharField()
    major = serializers.CharField()
    minor = serializers.CharField()
    concentration = serializers.CharField()

    class Meta:
        model = Education
        fields = (
            'id', 'school', 'start_date', 'end_date', 'degree', 'major', 'minor',
            'concentration')
