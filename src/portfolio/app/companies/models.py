from django.db import models

from portfolio.app.common.constants import STATES


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class Company(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(choices=STATES, max_length=2)
    # TODO: Migrate to django-filer
    logo = models.ImageField(upload_to=upload_to, null=True)
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
