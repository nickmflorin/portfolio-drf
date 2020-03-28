from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from portfolio.app.common.models import PortfolioModel


class Project(PortfolioModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
