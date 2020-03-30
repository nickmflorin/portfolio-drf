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
    name = models.CharField(max_length=64, unique=True,
        help_text="Verbose name for the file that will be used to display "
        "the downloadable or viewable file."
    )
    short_description = models.CharField(max_length=256)
    long_description = models.CharField(max_length=1024)
    caption = models.CharField(max_length=256, null=True, blank=True,
        help_text="Caption for image files.  Only allowed/required when the "
        "file is an image file."
    )
    project = models.ForeignKey('projects.Project',
        on_delete=models.CASCADE, related_name='files')


class Project(PortfolioModel):
    name = models.CharField(max_length=64, unique=True, help_text=(
        "Name of the project."
    ))
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
    display_alone = models.BooleanField(default=True, help_text=(
        "Determines whether or not the project will be displayed on the "
        "projects page as it's own item."
    ))
