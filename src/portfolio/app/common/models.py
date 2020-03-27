from django.db import models

from .constants import MONTHS, YEARS


class PortfolioModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True, db_index=True)
    date_modified = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class HorizonModel(PortfolioModel):
    start_month = models.IntegerField(choices=MONTHS, null=False, blank=False)
    start_year = models.IntegerField(choices=YEARS, null=False, blank=False)
    end_month = models.IntegerField(
        choices=MONTHS,
        null=True,
        blank=True
    )
    end_year = models.IntegerField(
        choices=YEARS,
        null=True,
        blank=True
    )
    current = models.BooleanField(default=False)

    class Meta:
        abstract = True
