from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from portfolio.app.common.models import HorizonModel
from portfolio.app.projects.models import Project


class Education(HorizonModel):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
    degree = models.CharField(max_length=64, unique=False)
    major = models.CharField(max_length=64, unique=False)
    minor = models.CharField(max_length=64, unique=True, null=True, blank=True)
    concentration = models.CharField(max_length=64, null=True, blank=True)
    gpa = models.FloatField(null=True)
    description = RichTextField(
        config_name='description',
        null=True,
        blank=True
    )
    include_in_resume = models.BooleanField(
        default=True,
        help_text=(
            "Determines whether or not the experience will be included in the "
            "auto generated resume."
        )
    )
    projects = GenericRelation(Project)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school.name}"
