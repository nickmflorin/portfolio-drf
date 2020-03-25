from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.name
