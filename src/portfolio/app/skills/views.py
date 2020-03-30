from rest_framework import viewsets
from rest_framework.response import Response

from .models import Skill
from .serializers import SkillSerializer, BasicSkillSerializer


class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def list(self, *args):
        data = BasicSkillSerializer(self.queryset, many=True).data
        return Response(data)
