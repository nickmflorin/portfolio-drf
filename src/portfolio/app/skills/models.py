from django.db import models
from django.db.models.signals import m2m_changed

from portfolio.app.common.models import PortfolioModel
import logging

logger = logging.getLogger('portfolio')


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


def nested_skills_added(sender, **kwargs):
    from portfolio.app.courses.models import Course
    from portfolio.app.projects.models import Project

    if kwargs['action'] == 'post_add':
        # If skills were added to a project, we want to make sure the skills are
        # also added to the education or experience with this project. Saving the
        # project will force the skills to be added to the education or experience
        # in the overridden save method.
        instance = kwargs['instance']
        if isinstance(instance, (Project, Course)):
            instance.save()


m2m_changed.connect(nested_skills_added, sender=Skill.projects.through)
m2m_changed.connect(nested_skills_added, sender=Skill.courses.through)
