import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_school):
    schools = [
        create_school(),
        create_school()
    ]
    response = api_client.get('/api/v1/schools/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': schools[0].pk,
            'name': schools[0].name,
            'description': schools[0].description,
            'city': schools[0].city,
            'state': schools[0].state,
            'logo': None,
        },
        {
            'id': schools[1].pk,
            'name': schools[1].name,
            'description': schools[1].description,
            'city': schools[1].city,
            'state': schools[1].state,
            'logo': None,
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_school):
    school = create_school()
    response = api_client.get('/api/v1/schools/%s/' % school.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': school.pk,
        'name': school.name,
        'description': school.description,
        'city': school.city,
        'state': school.state,
        'logo': None,
    }
