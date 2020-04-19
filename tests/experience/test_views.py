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
        'include_in_resume': True,
        'description': experience.description,
        'title': experience.title,
        'short_title': experience.short_title,
        'date_modified': experience.date_modified.strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': experience.date_created.strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        'company': {
            'id': experience.company.pk,
            'name': experience.company.name,
            'city': experience.company.city,
            'state': experience.company.state,
            'logo': None,
            'url': experience.company.url,
            'description': experience.company.description,
            'date_modified': experience.company.date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': experience.company.date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
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
        'include_in_resume': True,
        'description': experience.description,
        'title': experience.title,
        'short_title': experience.short_title,
        'date_modified': experience.date_modified.strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': experience.date_created.strftime(
            "%Y-%m-%dT%H:%M:%S.%fZ"),
        'company': {
            'id': experience.company.pk,
            'name': experience.company.name,
            'city': experience.company.city,
            'state': experience.company.state,
            'logo': None,
            'url': experience.company.url,
            'description': experience.company.description,
            'date_modified': experience.company.date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': experience.company.date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
        },
        'skills': [
            {
                'id': skill.pk,
                'name': skill.name,
                'date_modified': skill.date_modified.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
                'date_created': skill.date_created.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
            }
        ],
        'projects': [
            {
                'id': projects[0].pk,
                'name': projects[0].name,
                'description': projects[0].description,
                'showcase': False,
                'include_in_resume': True,
                'date_modified': projects[0].date_modified.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
                'date_created': projects[0].date_created.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
            },
            {
                'id': projects[1].pk,
                'name': projects[1].name,
                'description': projects[1].description,
                'showcase': False,
                'include_in_resume': True,
                'date_modified': projects[1].date_modified.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
                'date_created': projects[1].date_created.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
            }
        ]
    }
