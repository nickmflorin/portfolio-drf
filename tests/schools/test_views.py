import pytest

from portfolio.app.schools.models import School


@pytest.mark.django_db
def test_list_response_200(api_client):
    schools = [
        School.objects.create(
            name="RPI",
            city="Troy",
            state="NY"
        ),
        School.objects.create(
            name="Harvard",
            city="Boston",
            state="MA",
        )
    ]
    response = api_client.get('/api/v1/schools/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': schools[0].pk,
            'name': 'RPI',
            'description': None,
            'city': 'Troy',
            'state': 'NY',
            'logo': None,
        },
        {
            'id': schools[1].pk,
            'name': 'Harvard',
            'description': None,
            'city': 'Boston',
            'state': 'MA',
            'logo': None,
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client):
    school = School.objects.create(
        name="SUNY Buffalo",
        city="Buffalo",
        state="NY"
    )
    response = api_client.get('/api/v1/schools/%s/' % school.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': school.pk,
        'name': "SUNY Buffalo",
        'logo': None,
        'description': None,
        'city': 'Buffalo',
        'state': 'NY',
    }
