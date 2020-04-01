import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_experience, create_project,
        create_skill):
    experience = create_experience()
    response = api_client.get('/api/v1/experience/')
    assert response.json() == [{
        'id': experience.pk,
        'start_month': experience.start_month,
        'end_month': experience.end_month,
        'start_year': experience.start_year,
        'end_year': experience.end_year,
        'current': experience.current,
        'description': experience.description,
        'title': experience.title,
        'company': {
            'id': experience.company.pk,
            'name': experience.company.name,
            'city': experience.company.city,
            'state': experience.company.state,
            'logo': None,
            'url': experience.company.url,
            'description': experience.company.description,
        },
    }]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_experience, create_project,
        create_skill):
    experience = create_experience()
    projects = [
        create_project(experience=experience),
        create_project(experience=experience)
    ]
    skill = create_skill()
    skill.experiences.set([experience])

    response = api_client.get('/api/v1/experience/%s/' % experience.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': experience.pk,
        'start_month': experience.start_month,
        'end_month': experience.end_month,
        'start_year': experience.start_year,
        'end_year': experience.end_year,
        'current': experience.current,
        'description': experience.description,
        'title': experience.title,
        'company': {
            'id': experience.company.pk,
            'name': experience.company.name,
            'city': experience.company.city,
            'state': experience.company.state,
            'logo': None,
            'url': experience.company.url,
            'description': experience.company.description,
        },
        'skills': [
            {
                'id': skill.pk,
                'name': skill.name,
            }
        ],
        'projects': [
            {
                'id': projects[0].pk,
                'name': projects[0].name,
                'short_description': projects[0].short_description,
                'showcase': False,
            },
            {
                'id': projects[1].pk,
                'name': projects[1].name,
                'short_description': projects[1].short_description,
                'showcase': False,
            }
        ]
    }
