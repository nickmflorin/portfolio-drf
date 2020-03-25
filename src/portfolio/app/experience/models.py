from django.db import models

from portfolio.app.common.models import HorizonModel


class Experience(HorizonModel):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    title = models.CharField(
        max_length=64,
        help_text="Name of your role at the company."
    )
    description = models.CharField(max_length=512, null=True, blank=True)

    projects = models.ManyToManyField('projects.Project',
        blank=True,
        related_name='%(app_label)s_%(class)s_projects',
        help_text="Projects worked on during employment."
    )

    skills = models.ManyToManyField('skills.Skill',
        blank=True,
        related_name='%(app_label)s_%(class)s_skills',
        help_text="Skilled worked on during employment."
    )

    class Meta:
        verbose_name_plural = "Experience History"

    def __str__(self):
        return f"{self.title} at {self.company.name}"
