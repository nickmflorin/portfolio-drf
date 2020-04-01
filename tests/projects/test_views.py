import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_project,
        create_skill, create_education):
    projects = [
        create_project(),
        create_project()
    ]
    response = api_client.get('/api/v1/projects/')
    assert response.status_code == 200
    assert response.json() == [
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


@pytest.mark.django_db
def test_detail_response_200_with_education(api_client, create_project, create_skill,
        create_education):

    education = create_education()
    project = create_project(education=education)
    skill = create_skill()
    skill.projects.add(project)

    response = api_client.get('/api/v1/projects/%s/' % project.pk)
    assert response.status_code == 200
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
        }],
        'education': {
            'id': education.pk,
            'start_month': education.start_month,
            'end_month': education.end_month,
            'start_year': education.start_year,
            'end_year': education.end_year,
            'current': education.current,
            'degree': education.degree,
            'major': education.major,
            'gpa': education.gpa,
            'minor': education.minor,
            'concentration': education.concentration,
            'description': education.description,
            'school': {
                'id': education.school.pk,
                'name': education.school.name,
                'city': education.school.city,
                'state': education.school.state,
                'logo': None,
                'description': education.school.description,
            },
        }
    }


@pytest.mark.django_db
def test_detail_response_200_with_experience(api_client, create_project, create_skill,
        create_experience):

    experience = create_experience()
    project = create_project(experience=experience)
    skill = create_skill()
    skill.projects.add(project)

    response = api_client.get('/api/v1/projects/%s/' % project.pk)
    assert response.status_code == 200
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
        }],
        'experience': {
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
        }
    }
