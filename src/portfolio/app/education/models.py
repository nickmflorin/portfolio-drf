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
    description = RichTextField(config_name='description')
    projects = GenericRelation(Project)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school.name}"

    def save(self, *args, **kwargs):
        """
        On save, we want to add any skills that were added to the projects or
        courses to also be added to the Education instance.

        NOTE:
        ----
        This is problematic if we are removing skills from a project or course,
        because there is no way to know whether the skill belonged to the
        Education instance via a Project, Course or added separately.

        A better long term implementation might be to use the m2m_changed signal.
        """
        for project in self.projects.all():
            for skill in project.skills.all():
                # Might have to put try except, can't access self.skills before
                # model has pk and is saved.
                if skill not in self.skills.all():
                    self.skills.add(skill)
        for course in self.courses.all():
            for skill in course.skills.all():
                # Might have to put try except, can't access self.skills before
                # model has pk and is saved.
                if skill not in self.skills.all():
                    self.skills.add(skill)
        super(Education, self).save(*args, **kwargs)
