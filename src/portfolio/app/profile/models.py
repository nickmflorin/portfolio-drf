from django.db import models

from portfolio.app.common.models import PortfolioModel


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"
    return f'uploads/resumes/{filename}'


class Profile(PortfolioModel):
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    middle_name = models.CharField(max_length=24)
    email = models.EmailField(max_length=24)
    github_url = models.URLField(max_length=100)
    linkedin_url = models.URLField(max_length=100)
    resume = models.FileField(upload_to=upload_to, null=True)
