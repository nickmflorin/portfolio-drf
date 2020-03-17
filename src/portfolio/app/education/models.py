from django.db import models


class School(models.Model):
    name = models.CharField(max_length=64, unique=False)
    city = models.CharField(max_length=64, unique=False)
    state = models.CharField(max_length=2, unique=False)
    logo = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self):
        return self.name


class Education(models.Model):
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE,
    )
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=True, blank=True)
    degree = models.CharField(max_length=64, unique=False)
    major = models.CharField(max_length=64, unique=False)
    minor = models.CharField(max_length=64, unique=True, null=True, blank=True)
    concentration = models.CharField(max_length=64, unique=True, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school.name}"
