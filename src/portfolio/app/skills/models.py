from django.db import models

from portfolio.app.common.models import PortfolioModel


class Skill(PortfolioModel):
    name = models.CharField(max_length=64)
    educations = models.ManyToManyField('education.Education', blank=True,)
    experiences = models.ManyToManyField('experience.Experience', blank=True)
    # courses = models.ManyToManyField('courses.Course', blank=True)
