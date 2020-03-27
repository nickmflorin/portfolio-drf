from django.db import models

from portfolio.app.common.models import PortfolioModel


class Course(PortfolioModel):
    name = models.CharField(max_length=64, unique=False,
        help_text="Name of the course or class.")
    description = models.CharField(max_length=512, null=True, blank=True)
    education = models.ForeignKey('education.Education',
        on_delete=models.CASCADE, related_name='courses')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        On save, we want to force the associated education to save
        as well, so that any skills added to this course will also be
        added to the education.

        NOTE:
        ----
        We need to investigate whether or not the extra saving is necessary,
        because the forms might handle the save of the related model themselves.
        """
        self.education.save()
        super(Course, self).save(*args, **kwargs)
