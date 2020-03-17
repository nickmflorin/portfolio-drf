import pytest

from portfolio.app.skills.models import Skill


@pytest.mark.django_db
def test_list_response_200(api_client):
    skills = [
        Skill.objects.create(name="Python"),
        Skill.objects.create(name="Javascript")
    ]

    response = api_client.get('/api/v1/skills/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': skills[0].pk,
            'name': 'Python'
        },
        {
            'id': skills[1].pk,
            'name': 'Javascript'
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client):
    skill = Skill.objects.create(name="Python")

    response = api_client.get('/api/v1/skills/%s/' % skill.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': skill.pk,
        'name': 'Python'
    }
