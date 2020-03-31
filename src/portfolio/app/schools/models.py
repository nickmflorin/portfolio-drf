from django.db import models

from portfolio.app.common.models import PortfolioModel
from portfolio.app.common.constants import STATES


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class School(PortfolioModel):
    name = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=64, help_text=(
        "City that the school is located in."
    ))
    state = models.CharField(choices=STATES, max_length=2, help_text=(
        "State that the school is located in."
    ))
    logo = models.ImageField(upload_to=upload_to, null=True)
    description = models.CharField(max_length=512, null=True, blank=True)
