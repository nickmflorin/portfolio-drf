from django.db import models


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class Company(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    logo = models.ImageField(upload_to=upload_to, null=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)
    projects = models.ManyToManyField('projects.Project',
        blank=True,
        related_name='%(app_label)s_%(class)s_projects',
        help_text="Projects worked on during employment.")

    def __str__(self):
        return f"{self.title} at {self.company.name}"
