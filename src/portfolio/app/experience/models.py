from django.db import models


class Experience(models.Model):
    company = models.ForeignKey('companies.Company', on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    current = models.BooleanField(default=False)

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
