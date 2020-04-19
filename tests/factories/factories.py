import factory
from django.contrib.contenttypes.models import ContentType

from portfolio.app.common.constants import STATES

from portfolio.app.comments.models import Comment
from portfolio.app.companies.models import Company
from portfolio.app.courses.models import Course
from portfolio.app.education.models import Education
from portfolio.app.experience.models import Experience
from portfolio.app.projects.models import Project
from portfolio.app.profile.models import Profile
from portfolio.app.schools.models import School
from portfolio.app.skills.models import Skill

from .base import PortfolioModelFactory


__all__ = (
    'CompanyFactory',
    'SchoolFactory',
    'EducationFactory',
    'ExperienceFactory',
    'CourseFactory',
    'ProjectFactory',
    'SkillFactory',
    'ProfileFactory',
    'CommentFactory',
)


class HorizonModelFactory(PortfolioModelFactory):
    start_month = 1
    end_month = 6
    start_year = 2010
    end_year = 2014

    class Meta:
        abstract = True


class CommentFactory(PortfolioModelFactory):
    name = factory.Faker('name')
    comment = factory.Faker('paragraph')
    email = factory.Faker('email')
    public = True

    class Meta:
        model = Comment


class ProfileFactory(PortfolioModelFactory):
    first_name = factory.Faker('name')
    last_name = factory.Faker('name')
    middle_name = factory.Faker('name')
    email = factory.Faker('email')
    github_url = factory.Faker('url')
    linkedin_url = factory.Faker('url')
    resume = factory.Faker('url')
    intro = factory.Faker('paragraph')
    tagline = factory.Faker('paragraph')
    address = factory.Faker('address')
    phone = factory.Faker('phone_number')

    class Meta:
        model = Profile


class CompanyFactory(PortfolioModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('paragraph')
    state = factory.Sequence(lambda n: STATES[n][0])
    city = factory.Faker('name')
    url = factory.Faker('url')
    logo = None

    class Meta:
        model = Company


class SchoolFactory(PortfolioModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('paragraph')
    state = factory.Sequence(lambda n: STATES[n][0])
    city = factory.Faker('name')
    logo = None

    class Meta:
        model = School


class EducationFactory(HorizonModelFactory):
    description = factory.Faker('paragraph')
    school = factory.SubFactory(SchoolFactory)
    major = factory.Faker('name')
    minor = factory.Faker('name')
    concentration = factory.Faker('name')
    gpa = factory.Iterator([3.1, 3.2, 3.3, 3.5, 3.8])

    class Meta:
        model = Education


class ExperienceFactory(HorizonModelFactory):
    title = factory.Faker('name')
    short_title = factory.Faker('name')
    description = factory.Faker('paragraph')
    company = factory.SubFactory(CompanyFactory)

    class Meta:
        model = Experience


class CourseFactory(PortfolioModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('paragraph')
    education = factory.SubFactory(EducationFactory)

    class Meta:
        model = Course


class ProjectFactory(PortfolioModelFactory):
    name = factory.Faker('name')
    description = factory.Faker('paragraph')
    showcase_description = factory.Faker('paragraph')
    resume_description = factory.Faker('paragraph')
    content_object = factory.SubFactory(EducationFactory)
    content_type = factory.LazyAttribute(
        lambda o: ContentType.objects.get_for_model(o.content_object))
    object_id = factory.SelfAttribute('content_object.pk')
    showcase = False

    class Meta:
        model = Project

    @classmethod
    def create(cls, *args, **kwargs):
        content_object = None
        if 'education' in kwargs:
            content_object = kwargs['education']
            del kwargs['education']
        elif 'experience' in kwargs:
            if 'education' in kwargs:
                raise Exception("Cannot provide both education and experience.")
            content_object = kwargs['experience']
            del kwargs['experience']

        if content_object:
            kwargs.update(
                content_object=content_object,
                object_id=content_object.pk,
            )
        return super(ProjectFactory, cls).create(*args, **kwargs)


class SkillFactory(PortfolioModelFactory):
    name = factory.Faker('name')

    class Meta:
        model = Skill
