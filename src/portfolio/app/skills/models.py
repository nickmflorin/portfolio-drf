from django.db import models

from portfolio.app.common.models import PortfolioModel


class Skill(PortfolioModel):
    name = models.CharField(max_length=64)
    educations = models.ManyToManyField('education.Education',
        blank=True, related_name='skills')
    experiences = models.ManyToManyField('experience.Experience',
        blank=True, related_name='skills')
    courses = models.ManyToManyField('courses.Course',
        blank=True, related_name='skills')
    projects = models.ManyToManyField('projects.Project',
        blank=True, related_name='skills')
