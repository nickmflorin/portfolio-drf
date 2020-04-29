from rest_framework import viewsets
from rest_framework.response import Response

from portfolio.app.education.models import Education
from portfolio.app.education.serializers import DetailEducationSerializer

from portfolio.app.experience.models import Experience
from portfolio.app.experience.serializers import DetailExperienceSerializer

from portfolio.app.skills.models import Skill
from portfolio.app.skills.serializers import NestedSkillSerializer


class ResumeViewSet(viewsets.ViewSet):

    def list(self, request):
        education = Education.objects.filter(include_in_resume=True).all()
        experience = Experience.objects.filter(include_in_resume=True).all()
        skills = Skill.objects.all()
        return Response({
            'education': DetailEducationSerializer(education, many=True).data,
            'experience': DetailExperienceSerializer(experience, many=True).data,
            'skills': NestedSkillSerializer(skills, many=True).data
        })
