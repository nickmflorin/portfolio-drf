from django.db import models


def upload_to(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{instance.name.lower().replace(' ','')}.{ext}"
    return f'uploads/{filename}'


class Company(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    logo = models.ImageField(upload_to=upload_to, null=True)

    def __str__(self):
        return self.name


class Experience(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
    )
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.title} at {self.company.name}"
