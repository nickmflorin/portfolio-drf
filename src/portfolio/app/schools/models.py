from django.db import models


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class School(models.Model):
    name = models.CharField(max_length=64, unique=False)
    city = models.CharField(max_length=64, unique=False)
    state = models.CharField(max_length=2, unique=False)
    # TODO: Migrate to django-filer
    logo = models.ImageField(upload_to=upload_to, null=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    def __str__(self):
        return self.name
