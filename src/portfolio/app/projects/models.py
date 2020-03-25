from django.db import models

from portfolio.app.common.models import PortfolioModel


class Project(PortfolioModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)
