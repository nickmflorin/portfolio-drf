import os
import pytest


@pytest.mark.django_db
def test_response_200(api_client, create_profile):
    profile = create_profile()
    response = api_client.get('/api/v1/profile/')
    assert response.status_code == 200
    assert response.json() == {
        'id': profile.id,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
        'middle_name': profile.middle_name,
        'email': profile.email,
        'github_url': profile.github_url,
        'linkedin_url': profile.linkedin_url,
        'resume': os.path.join('http://testserver', profile.resume.url[1:]),
        'intro': profile.intro,
        'date_modified': profile.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': profile.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    }
