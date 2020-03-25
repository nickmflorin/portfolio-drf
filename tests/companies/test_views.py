import pytest

from portfolio.app.companies.models import Company


@pytest.mark.django_db
def test_list_response_200(api_client):
    companies = [
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
    response = api_client.get('/api/v1/companies/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': companies[0].pk,
            'name': 'Google',
            'city': 'San Francisco',
            'state': 'CA',
            'logo': None,
            'description': 'A Tech Company'
        },
        {
            'id': companies[1].pk,
            'name': 'Walmart',
            'city': 'Boston',
            'state': 'MA',
            'logo': None,
            'description': 'A Retail Company'
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client):
    company = Company.objects.create(
        name="Google",
        city="San Francisco",
        state="CA",
        description="A Tech Company"
    )

    response = api_client.get('/api/v1/companies/%s/' % company.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': company.pk,
        'name': 'Google',
        'city': 'San Francisco',
        'state': 'CA',
        'logo': None,
        'description': 'A Tech Company'
    }
