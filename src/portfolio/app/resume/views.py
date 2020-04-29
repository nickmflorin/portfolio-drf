from rest_framework import viewsets
from rest_framework.response import Response

from portfolio.app.education.models import Education
from portfolio.app.education.serializers import DetailEducationSerializer

from portfolio.app.experience.models import Experience
from portfolio.app.experience.serializers import DetailExperienceSerializer

from portfolio.app.skills.models import Skill
from portfolio.app.skills.serializers import NestedSkillSerializer

from portfolio.app.profile.models import Profile
from portfolio.app.profile.serializers import ProfileSerializer


class ResumeViewSet(viewsets.ViewSet):

    def list(self, request):
        education = Education.objects.filter(include_in_resume=True).all()
        experience = Experience.objects.filter(include_in_resume=True).all()
        skills = Skill.objects.all()
        profile = Profile.objects.first()

        return Response({
            'education': DetailEducationSerializer(education, many=True,
                context={'request': request}).data,
            'experience': DetailExperienceSerializer(experience, many=True,
                context={'request': request}).data,
            'skills': NestedSkillSerializer(skills, many=True,
                context={'request': request}).data,
            'profile': ProfileSerializer(profile, context={'request': request}).data
        })
