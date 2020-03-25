from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=64, unique=False)
    description = models.CharField(max_length=512, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)
