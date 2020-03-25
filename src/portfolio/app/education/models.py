from django.db import models

from portfolio.app.common.models import HorizonModel


class Education(HorizonModel):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
    degree = models.CharField(max_length=64, unique=False)
    major = models.CharField(max_length=64, unique=False)
    minor = models.CharField(max_length=64, unique=True, null=True, blank=True)
    concentration = models.CharField(max_length=64, null=True, blank=True)
    gpa = models.FloatField(null=True)

    description = models.CharField(max_length=512, null=True, blank=True)

    projects = models.ManyToManyField('projects.Project',
        blank=True,
        related_name='%(app_label)s_%(class)s_projects',
        help_text="Projects worked on during education."
    )

    skills = models.ManyToManyField('skills.Skill',
        blank=True,
        related_name='%(app_label)s_%(class)s_skills',
        help_text="Skilled worked on during education."
    )

    class Meta:
        verbose_name_plural = "Education History"

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school.name}"
