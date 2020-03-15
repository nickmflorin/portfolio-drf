import pytest


@pytest.mark.django_db
def test_list_response_200(api_client):
    response = api_client.get('/api/v1/skills/')
    assert response.status_code == 200
