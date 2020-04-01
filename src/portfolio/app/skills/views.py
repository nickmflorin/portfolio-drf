from portfolio.app.common.views import PartitionedReadOnlyViewSet

from .models import Skill
from .serializers import DetailSkillSerializer, ListSkillSerializer


class SkillViewSet(PartitionedReadOnlyViewSet):
    queryset = Skill.objects.all()
    list_serializer_class = ListSkillSerializer
    detail_serializer_class = DetailSkillSerializer
