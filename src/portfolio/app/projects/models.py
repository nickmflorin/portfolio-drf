from ckeditor.fields import RichTextField

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from portfolio.app.common.models import PortfolioModel


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return f'uploads/projects/{instance.project.name}/{filename}'


class ProjectFile(PortfolioModel):
    file = models.FileField(upload_to=upload_to, null=True)
    name = models.CharField(
        max_length=64,
        help_text=(
            "Human readable name for the file that will be displayed to users "
            "in links to download or access the file."
        )
    )
    description = RichTextField(config_name='description', null=True, blank=True)
    caption = RichTextField(
        null=True,
        blank=True,
        config_name='caption',
        help_text=(
            "Caption for image files.  Only allowed/required when the "
            "file is an image file."
        )
    )
    project = models.ForeignKey('projects.Project',
        on_delete=models.CASCADE, related_name='files')
    relative_order = models.IntegerField(default=0)


class Project(PortfolioModel):
    name = models.CharField(max_length=64, unique=True)
    description = RichTextField(config_name='description')
    showcase_description = RichTextField(
        null=True,
        blank=True,
        config_name='long_description',
        help_text=(
            "Long description of the project to be used when the project is showcased. "
            "Only allowed, but also required, if showcase is checked."
        )
    )
    content_type = models.ForeignKey(ContentType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        limit_choices_to={'model__in': (
            'education.Education',
            'experience.Experience',
        )}
    )
    object_id = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    content_object = GenericForeignKey('content_type', 'object_id')
    showcase = models.BooleanField(
        default=False,
        help_text=(
            "Determines whether or not the project will be showcased on the "
            "projects page.  If showcasing a project, the project must include "
            "at least 1 image file."
        ))
