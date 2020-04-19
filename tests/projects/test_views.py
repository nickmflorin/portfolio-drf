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
        'description': project.description,
        'showcase_description': project.showcase_description,
        'resume_description': project.resume_description,
        'showcase': False,
        'include_in_resume': True,
        'files': [],
        'date_modified': project.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': project.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'skills': [{
            'id': skill.pk,
            'name': skill.name,
            'date_modified': skill.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': skill.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }],
        'education': {
            'id': education.pk,
            'start_month': education.start_month,
            'end_month': education.end_month,
            'start_year': education.start_year,
            'end_year': education.end_year,
            'current': education.current,
            'include_in_resume': True,
            'include_in_resume': True,
            'degree': education.degree,
            'major': education.major,
            'gpa': education.gpa,
            'minor': education.minor,
            'concentration': education.concentration,
            'description': education.description,
            'date_modified': education.date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': education.date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'school': {
                'id': education.school.pk,
                'name': education.school.name,
                'city': education.school.city,
                'state': education.school.state,
                'logo': None,
                'description': education.school.description,
                'date_modified': education.school.date_modified.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
                'date_created': education.school.date_created.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
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
        'description': project.description,
        'showcase_description': project.showcase_description,
        'resume_description': project.resume_description,
        'showcase': False,
        'include_in_resume': True,
        'files': [],
        'date_modified': project.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': project.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'skills': [{
            'id': skill.pk,
            'name': skill.name,
            'date_modified': skill.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': skill.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }],
        'experience': {
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
        }
    }
