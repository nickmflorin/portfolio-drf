from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    logo = models.ImageField(upload_to='uploads/', null=True)

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
