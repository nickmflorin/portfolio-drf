from django.db import models
from django.contrib.contenttypes.fields import GenericRelation

from portfolio.app.common.models import HorizonModel
from portfolio.app.projects.models import Project


class Education(HorizonModel):
    school = models.ForeignKey('schools.School', on_delete=models.CASCADE)
    degree = models.CharField(max_length=64, unique=False)
    major = models.CharField(max_length=64, unique=False)
    minor = models.CharField(max_length=64, unique=True, null=True, blank=True)
    concentration = models.CharField(max_length=64, null=True, blank=True)
    gpa = models.FloatField(null=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    projects = GenericRelation(Project)

    class Meta:
        verbose_name_plural = "Education History"

    def __str__(self):
        return f"{self.degree} in {self.major} from {self.school.name}"

    # TODO: Override save method so that skills for courses in this education are
    # also included.
    def save(self, *args, **kwargs):
        if self.id:
            skills = self.skills.all()
            for course in self.course_set.all():
                for course_skill in course.skills.all():
                    import ipdb; ipdb.set_trace()
        super(Education, self).save(*args, **kwargs)
