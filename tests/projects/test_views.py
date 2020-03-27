import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_project, create_skill):
    projects = [
        create_project(),
        create_project()
    ]
    skill = create_skill()
    skill.projects.add(projects[1])

    response = api_client.get('/api/v1/projects/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': projects[0].pk,
            'name': projects[0].name,
            'description': projects[0].description,
            'skills': [],
        },
        {
            'id': projects[1].pk,
            'name': projects[1].name,
            'description': projects[1].description,
            'skills': [{
                'id': skill.pk,
                'name': skill.name
            }]
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_project, create_skill):
    project = create_project()
    skill = create_skill()
    skill.projects.add(project)

    response = api_client.get('/api/v1/projects/%s/' % project.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': project.pk,
        'name': project.name,
        'description': project.description,
        'skills': [{
            'id': skill.pk,
            'name': skill.name
        }]
    }