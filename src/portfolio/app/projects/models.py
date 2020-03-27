from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

from portfolio.app.common.models import PortfolioModel


class Project(PortfolioModel):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=1024, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, *args, **kwargs):
        """
        On save, we want to force the associated education or experience to save
        as well, so that any skills added to this project will also be
        added to the education or experience.

        NOTE:
        ----
        We need to investigate whether or not the extra saving is necessary,
        because the forms might handle the save of the related model themselves.
        """
        self.content_object.save()
        super(Project, self).save(*args, **kwargs)
