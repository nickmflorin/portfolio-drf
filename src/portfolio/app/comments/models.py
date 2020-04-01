from django.db import models

from portfolio.app.common.models import PortfolioModel


class Comment(PortfolioModel):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32, null=True, blank=True)
    value = models.CharField(max_length=512)
    public = models.BooleanField(default=True)
