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
    name = models.CharField(
        max_length=64,
        unique=True,
        help_text=(
            "Human readable name for the file that will be displayed to users "
            "in links to download/access the file."
        )
    )
    description = models.CharField(max_length=1024)
    caption = models.CharField(max_length=256, null=True, blank=True)
    project = models.ForeignKey('projects.Project',
        on_delete=models.CASCADE, related_name='files')


class Project(PortfolioModel):
    name = models.CharField(max_length=64, unique=True)
    short_description = models.CharField(max_length=256)
    long_description = models.CharField(max_length=1024)
    content_type = models.ForeignKey(ContentType,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': (
            'education.Education',
            'experience.Experience',
        )}
    )
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    showcase = models.BooleanField(
        default=True,
        help_text=(
            "Determines whether or not the project will be showcased on the "
            "projects page."
        ))
