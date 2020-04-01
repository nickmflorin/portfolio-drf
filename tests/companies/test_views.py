import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_company):
    companies = [
        create_company(),
        create_company()
    ]
    response = api_client.get('/api/v1/companies/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': companies[0].pk,
            'name': companies[0].name,
            'city': companies[0].city,
            'state': companies[0].state,
            'logo': None,
            'url': companies[0].url,
            'description': companies[0].description,
            'date_modified': companies[0].date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': companies[0].date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        },
        {
            'id': companies[1].pk,
            'name': companies[1].name,
            'city': companies[1].city,
            'state': companies[1].state,
            'logo': None,
            'url': companies[1].url,
            'description': companies[1].description,
            'date_modified': companies[1].date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': companies[1].date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_company):
    company = create_company()
    response = api_client.get('/api/v1/companies/%s/' % company.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': company.pk,
        'name': company.name,
        'city': company.city,
        'state': company.state,
        'logo': None,
        'url': company.url,
        'description': company.description,
        'date_modified': company.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': company.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    }
