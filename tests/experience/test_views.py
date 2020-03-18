import datetime
import pytest

from portfolio.app.experience.models import Experience


@pytest.mark.django_db
def test_list_response_200(api_client, projects, companies):
    experience = Experience.objects.create(
        company=companies[0],
        start_date=datetime.datetime(2018, 1, 1),
        end_date=datetime.datetime(2020, 1, 1),
        title="Engineer",
        description="Some Experience",
    )
    experience.projects.set(projects)
    response = api_client.get('/api/v1/experience/')
    assert response.status_code == 200
    assert response.json() == [{
        'id': experience.pk,
        'start_date': '2018-01-01',
        'end_date': '2020-01-01',
        'title': 'Engineer',
        'description': 'Some Experience',
        'current': False,
        'company': {
            'id': companies[0].pk,
            'name': companies[0].name,
            'city': companies[0].city,
            'state': companies[0].state,
            'logo': None,
            'description': companies[0].description,
        },
        'projects': [
            {
                'id': projects[0].pk,
                'name': projects[0].name,
                'description': projects[0].description,
            },
            {
                'id': projects[1].pk,
                'name': projects[1].name,
                'description': projects[1].description,
            }
        ]
    }]


@pytest.mark.django_db
def test_detail_response_200(api_client, projects, companies):
    experience = Experience.objects.create(
        company=companies[0],
        start_date=datetime.datetime(2018, 1, 1),
        end_date=datetime.datetime(2020, 1, 1),
        title="Engineer",
        description="Some Experience",
    )
    experience.projects.set(projects)
    response = api_client.get('/api/v1/experience/%s/' % experience.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': experience.pk,
        'start_date': '2018-01-01',
        'end_date': '2020-01-01',
        'title': 'Engineer',
        'description': 'Some Experience',
        'current': False,
        'company': {
            'id': companies[0].pk,
            'name': companies[0].name,
            'city': companies[0].city,
            'state': companies[0].state,
            'logo': None,
            'description': companies[0].description,
        },
        'projects': [
            {
                'id': projects[0].pk,
                'name': projects[0].name,
                'description': projects[0].description,
            },
            {
                'id': projects[1].pk,
                'name': projects[1].name,
                'description': projects[1].description,
            }
        ]
    }
