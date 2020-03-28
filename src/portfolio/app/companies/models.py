from django.db import models

from portfolio.app.common.models import PortfolioModel
from portfolio.app.common.constants import STATES


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class Company(PortfolioModel):
    name = models.CharField(max_length=64, unique=True)
    logo = models.ImageField(upload_to=upload_to, null=True)
    url = models.URLField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = models.CharField(choices=STATES, max_length=2)
    description = models.CharField(max_length=512, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name
