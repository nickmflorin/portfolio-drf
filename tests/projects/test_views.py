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
            'short_description': projects[0].short_description,
            'long_description': projects[0].long_description,
            'showcase': False,
            'files': [],
            'skills': [],
        },
        {
            'id': projects[1].pk,
            'name': projects[1].name,
            'short_description': projects[1].short_description,
            'long_description': projects[1].long_description,
            'showcase': False,
            'files': [],
            'skills': [{
                'id': skill.pk,
                'name': skill.name
            }]
        }
    ]


@pytest.mark.django_db
def test_detail_response_200_with_education(api_client, create_project,
        create_skill, create_education):

    education = create_education()
    project = create_project(education=education)
    skill = create_skill()
    skill.projects.add(project)

    response = api_client.get('/api/v1/projects/%s/' % project.pk)
    assert response.status_code == 200
    import json
    print(json.dumps(response.json(), indent=4))
    import ipdb; ipdb.set_trace()
    assert response.json() == {
        'id': project.pk,
        'name': project.name,
        'short_description': project.short_description,
        'long_description': project.long_description,
        'showcase': False,
        'files': [],
        'skills': [{
            'id': skill.pk,
            'name': skill.name
        }]
    }
