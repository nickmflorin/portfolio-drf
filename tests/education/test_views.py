import datetime
import pytest

from portfolio.app.education.models import Education, School


@pytest.mark.django_db
def test_list_response_200(api_client):
    school = School.objects.create(
        name="Harvard",
        city="Boston",
        state="MA"
    )
    Education.objects.create(
        school=school,
        start_date=datetime.datetime(2020, 1, 1),
        degree="BS",
        major="Engineering",
    )
    response = api_client.get('/api/v1/education/')
    assert response.status_code == 200
    assert response.json() == [{
        'id': 1,
        'start_date': '2020-01-01T00:00:00Z',
        'end_date': None,
        'degree': 'BS',
        'major': 'Engineering',
        'minor': None,
        'concentration': None,
        'school': {
            'id': 1,
            'name': 'Harvard',
            'city': 'Boston',
            'state': 'MA',
        }
    }]


@pytest.mark.django_db
def test_detail_response_200(api_client):
    school = School.objects.create(
        name="Harvard",
        city="Boston",
        state="MA"
    )
    education = Education.objects.create(
        school=school,
        start_date=datetime.datetime(2020, 1, 1),
        degree="BS",
        major="Engineering",
    )
    response = api_client.get('/api/v1/education/%s/' % education.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'start_date': '2020-01-01T00:00:00Z',
        'end_date': None,
        'degree': 'BS',
        'major': 'Engineering',
        'minor': None,
        'concentration': None,
        'school': {
            'id': 1,
            'name': 'Harvard',
            'city': 'Boston',
            'state': 'MA',
        }
    }
