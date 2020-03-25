from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=64, unique=False)
    description = models.CharField(max_length=512, null=True, blank=True)
