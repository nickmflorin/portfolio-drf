from rest_framework import viewsets

from portfolio.app.common.views import PartitionedViewSetMixin

from .models import Skill
from .serializers import DetailSkillSerializer, ListSkillSerializer


class SkillViewSet(PartitionedViewSetMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    list_serializer_class = ListSkillSerializer
    detail_serializer_class = DetailSkillSerializer
