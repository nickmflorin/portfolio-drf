import datetime
import pytest

from portfolio.app.experience.models import Experience, Company


@pytest.mark.django_db
def test_list_response_200(api_client):
    company = Company.objects.create(
        name="Google",
        city="San Francisco",
        state="CA"
    )
    experience = Experience.objects.create(
        company=company,
        start_date=datetime.datetime(2018, 1, 1),
        end_date=datetime.datetime(2020, 1, 1),
        title="Engineer",
    )
    response = api_client.get('/api/v1/experience/')
    assert response.status_code == 200
    assert response.json() == [{
        'id': experience.pk,
        'start_date': '2018-01-01T00:00:00Z',
        'end_date': '2020-01-01T00:00:00Z',
        'title': 'Engineer',
        'company': {
            'id': company.pk,
            'name': 'Google',
            'city': 'San Francisco',
            'state': 'CA',
        }
    }]


@pytest.mark.django_db
def test_detail_response_200(api_client):
    company = Company.objects.create(
        name="Google",
        city="San Francisco",
        state="CA"
    )
    experience = Experience.objects.create(
        company=company,
        start_date=datetime.datetime(2018, 1, 1),
        end_date=datetime.datetime(2020, 1, 1),
        title="Engineer",
    )
    response = api_client.get('/api/v1/experience/%s/' % experience.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': experience.pk,
        'start_date': '2018-01-01T00:00:00Z',
        'end_date': '2020-01-01T00:00:00Z',
        'title': 'Engineer',
        'company': {
            'id': company.pk,
            'name': 'Google',
            'city': 'San Francisco',
            'state': 'CA',
        }
    }
