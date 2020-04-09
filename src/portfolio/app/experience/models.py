from ckeditor.fields import RichTextField
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from portfolio.app.common.models import HorizonModel
from portfolio.app.projects.models import Project


class Experience(HorizonModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=64,
        help_text="Name of your role at the company."
    )
    description = RichTextField(config_name='description')
    projects = GenericRelation(Project)

    class Meta:
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.title} at {self.company.name}"
