import datetime
import pytest

from portfolio.app.education.models import Education


@pytest.mark.django_db
def test_list_response_200(api_client, projects, schools):
    education = Education.objects.create(
        school=schools[0],
        start_date=datetime.datetime(2020, 1, 1),
        degree="BS",
        major="Engineering",
        ongoing=True,
        description="A Really Good Degree If You Want to Have No Life",
    )
    education.projects.set(projects)

    response = api_client.get('/api/v1/education/')
    assert response.status_code == 200
    assert response.json() == [{
        'id': 1,
        'start_date': '2020-01-01',
        'end_date': None,
        'degree': 'BS',
        'major': 'Engineering',
        'gpa': None,
        'minor': None,
        'concentration': None,
        'ongoing': True,
        'description': "A Really Good Degree If You Want to Have No Life",
        'school': {
            'id': schools[0].pk,
            'name': schools[0].name,
            'city': schools[0].city,
            'state': schools[0].state,
            'logo': schools[0].logo,
            'description': schools[0].description,
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
def test_detail_response_200(api_client, projects, schools):
    education = Education.objects.create(
        school=schools[0],
        start_date=datetime.datetime(2020, 1, 1),
        degree="BS",
        major="Engineering",
        ongoing=True,
        description="A Really Good Degree If You Want to Have No Life",
    )
    education.projects.set(projects)
    response = api_client.get('/api/v1/education/%s/' % education.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'start_date': '2020-01-01',
        'end_date': None,
        'degree': 'BS',
        'major': 'Engineering',
        'gpa': None,
        'minor': None,
        'concentration': None,
        'ongoing': True,
        'description': "A Really Good Degree If You Want to Have No Life",
        'school': {
            'id': schools[0].pk,
            'name': schools[0].name,
            'city': schools[0].city,
            'state': schools[0].state,
            'logo': schools[0].logo,
            'description': schools[0].description,
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
