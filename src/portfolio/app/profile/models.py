from django.db import models

from portfolio.app.common.models import PortfolioModel


def upload_resume_to(instance, filename):
    return f'uploads/profile/resumes/{filename}'


def upload_headshot_to(instance, filename):
    return f'uploads/profile/headshots/{filename}'


def upload_logo_to(instance, filename):
    return f'uploads/profile/brand/{filename}'


class Profile(PortfolioModel):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=24)
    address = models.CharField(max_length=128, null=True, blank=True)
    # TODO: Come up with a better field for this.
    phone = models.CharField(max_length=10, null=True, blank=True)
    github_url = models.URLField(max_length=100)
    linkedin_url = models.URLField(max_length=100)
    resume = models.FileField(upload_to=upload_resume_to, null=True)
    headshot = models.ImageField(upload_to=upload_headshot_to, null=True)
    logo = models.ImageField(upload_to=upload_logo_to)
    intro = models.CharField(max_length=512)
    tagline = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
