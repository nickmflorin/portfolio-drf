import pytest

from portfolio.app.courses.models import Course


@pytest.mark.django_db
def test_list_response_200(api_client):
    courses = [
        Course.objects.create(name="Python"),
        Course.objects.create(name="Javascript")
    ]
    response = api_client.get('/api/v1/courses/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': courses[0].pk,
            'name': 'Python',
            'description': None,
        },
        {
            'id': courses[1].pk,
            'name': 'Javascript',
            'description': None,
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client):
    course = Course.objects.create(name="Python")
    response = api_client.get('/api/v1/courses/%s/' % course.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': course.pk,
        'name': 'Python',
        'description': None,
    }
