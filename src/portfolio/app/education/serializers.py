from rest_framework import serializers
from .models import School, Education


class SchoolSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    city = serializers.CharField()
    state = serializers.CharField()

    class Meta:
        model = School
        fields = ('name', 'city', 'state', )


class EducationSerializer(serializers.Serializer):
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
            'school', 'start_date', 'end_date', 'degree', 'major', 'minor',
            'concentration')
