from django.db import models


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class School(models.Model):
    name = models.CharField(max_length=64, unique=False)
    city = models.CharField(max_length=64, unique=False)
    state = models.CharField(max_length=2, unique=False)
    logo = models.ImageField(upload_to=upload_to, null=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=True, blank=True)
    degree = models.CharField(max_length=64, unique=False)
    major = models.CharField(max_length=64, unique=False)
    minor = models.CharField(max_length=64, unique=True, null=True, blank=True)
    concentration = models.CharField(max_length=64, unique=True, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    ongoing = models.BooleanField(default=False)
    projects = models.ManyToManyField('projects.Project',
        blank=True,
        related_name='%(app_label)s_%(class)s_projects',
        help_text="Projects worked on during education.")

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school.name}"
