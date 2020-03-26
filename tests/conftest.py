import pytest
from rest_framework.test import APIClient

from portfolio.app.courses.models import Course
from portfolio.app.schools.models import School
from portfolio.app.companies.models import Company
from portfolio.app.projects.models import Project
from portfolio.app.skills.models import Skill

from tests.factories import factories


@pytest.fixture
def api_client(monkeypatch):
    """
    Custom API Client that we will use to monkeypatch around edge cases if we
    need it.  We will most likely need to do this so this is a good starting
    point.
    """
    class CustomApiClient(APIClient):
        pass

    return CustomApiClient()


def inject_factory_fixtures():
    """
    This method will dynamically create factory fixtures for all of the
    factories present in the factories module.

    If we have a factory:
    >>> class SomeFactory():
    >>>     ...

    Then, a fixture will be generated with the name `some` which can be used
    as:

    >>> def test_something(create_some):
    >>>     model = create_some(attr1='foo', attr2='bar')
    """
    def model_factory_fixture_generator(factory_cls):
        @pytest.fixture(scope='module')
        def factory_fixture():
            def factory_generator(**kwargs):
                return factory_cls(**kwargs)
            return factory_generator
        return factory_fixture

    for factory_name in factories.__dict__['__all__']:
        factory_cls = factories.__dict__[factory_name]
        name = f"create_{factory_name.split('Factory')[0].lower()}"
        globals()[name] = model_factory_fixture_generator(factory_cls)


inject_factory_fixtures()


@pytest.fixture
@pytest.mark.django_db
def projects():
    return [
        Project.objects.create(
            name="Project 1",
            description="Some Project",
        ),
        Project.objects.create(
            name="Project 2",
            description="Some Other Project",
        )
    ]


@pytest.fixture
@pytest.mark.django_db
def schools():
    return [
        School.objects.create(
            name="Harvard",
            city="Boston",
            state="MA",
            description="Ivy League School",
        ),
        School.objects.create(
            name="University of Connecticut",
            city="Danbury",
            state="CT",
            description="State School",
        )
    ]


@pytest.fixture
@pytest.mark.django_db
def companies():
    return [
        Company.objects.create(
            name="Google",
            city="San Francisco",
            state="CA",
            description="A Tech Company",
        ),
        Company.objects.create(
            name="Walmart",
            city="Boston",
            state="MA",
            description="A Retail Company",
        ),
    ]


@pytest.fixture
@pytest.mark.django_db
def skills():
    return [
        Skill.objects.create(name='Programming'),
        Skill.objects.create(name='HTML'),
    ]


@pytest.fixture
@pytest.mark.django_db
def courses():
    return [
        Course.objects.create(name='Computer Science'),
        Course.objects.create(name='Calculus'),
    ]
