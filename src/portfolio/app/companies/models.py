from django.db import models


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class Company(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    # TODO: Migrate to django-filer
    logo = models.ImageField(upload_to=upload_to, null=True)
    description = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
