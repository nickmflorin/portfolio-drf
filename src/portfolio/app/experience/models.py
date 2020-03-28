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
    description = models.CharField(max_length=512, null=True, blank=True)
    projects = GenericRelation(Project)

    class Meta:
        verbose_name_plural = "Experience"

    def __str__(self):
        return f"{self.title} at {self.company.name}"

    def save(self, *args, **kwargs):
        """
        On save, we want to add any skills that were added to the projects
        to also be added to the Experience instance.

        NOTE:
        ----
        This is problematic if we are removing skills from a project or course,
        because there is no way to know whether the skill belonged to the
        Experience instance via a Project or added separately.

        A better long term implementation might be to use the m2m_changed signal.
        """
        for project in self.projects.all():
            for skill in project.skills.all():
                # Might have to put try except, can't access self.skills before
                # model has pk and is saved.
                if skill not in self.skills.all():
                    self.skills.add(skill)
        super(Experience, self).save(*args, **kwargs)
