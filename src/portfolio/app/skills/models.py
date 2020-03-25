from django.db import models

from portfolio.app.common.models import PortfolioModel


class Skill(PortfolioModel):
    name = models.CharField(max_length=64)
