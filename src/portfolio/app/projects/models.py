from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from portfolio.app.common.models import PortfolioModel


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return f'uploads/projects/{filename}'


class ProjectFile(PortfolioModel):
    file = models.FileField(upload_to=upload_to, null=True)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)
    project = models.ForeignKey('projects.Project',
        on_delete=models.CASCADE, related_name='files')


class Project(PortfolioModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
