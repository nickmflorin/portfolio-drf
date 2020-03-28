from django.db import models

from portfolio.app.common.models import PortfolioModel


class Course(PortfolioModel):
    name = models.CharField(max_length=64, unique=True,
        help_text="Name of the course or class.")
    description = models.CharField(max_length=512, null=True, blank=True)
    education = models.ForeignKey('education.Education',
        on_delete=models.CASCADE, related_name='courses')
