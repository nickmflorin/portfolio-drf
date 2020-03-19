import pytest
from rest_framework.test import APIClient

from portfolio.app.education.models import School
from portfolio.app.experience.models import Company
from portfolio.app.projects.models import Project
from portfolio.app.skills.models import Skill


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
