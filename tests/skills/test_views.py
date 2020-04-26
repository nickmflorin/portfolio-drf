import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_skill):
    skills = [
        create_skill(),
        create_skill()
    ]
    response = api_client.get('/api/v1/skills/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': skills[0].pk,
            'name': skills[0].name,
            'date_modified': skills[0].date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': skills[0].date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
        },
        {
            'id': skills[1].pk,
            'name': skills[1].name,
            'date_modified': skills[1].date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': skills[1].date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_skill, create_education,
        create_course, create_experience, create_project):
    skill = create_skill()
    project = create_project()
    education = create_education()
    experience = create_experience()
    courses = [
        create_course(education=education),
        create_course(education=education)
    ]
    skill.courses.set(courses)
    skill.experiences.add(experience)
    skill.educations.add(education)
    skill.projects.add(project)

    response = api_client.get('/api/v1/skills/%s/' % skill.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': skill.pk,
        'name': skill.name,
        'date_modified': skill.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': skill.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'educations': [{
            'id': education.pk,
            'start_month': education.start_month,
            'end_month': education.end_month,
            'start_year': education.start_year,
            'end_year': education.end_year,
            'current': education.current,
            'include_in_resume': True,
            'degree': education.degree,
            'major': education.major,
            'minor': education.minor,
            'concentration': education.concentration,
            'description': education.description,
            'gpa': education.gpa,
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
        }],
        'projects': [{
            'id': project.id,
            'name': project.name,
            'description': project.description,
            'showcase': False,
            'include_in_resume': True,
            'resume_description': project.resume_description,
            'date_modified': project.date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': project.date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
        }],
        'courses': [
            {
                'id': courses[0].pk,
                'name': courses[0].name,
                'description': courses[0].description,
                'date_modified': courses[0].date_modified.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
                'date_created': courses[0].date_created.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
            },
            {
                'id': courses[1].pk,
                'name': courses[1].name,
                'description': courses[1].description,
                'date_modified': courses[1].date_modified.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
                'date_created': courses[1].date_created.strftime(
                    "%Y-%m-%dT%H:%M:%S.%fZ"),
            }
        ],
        'experiences': [{
            'id': experience.pk,
            'start_month': experience.start_month,
            'end_month': experience.end_month,
            'start_year': experience.start_year,
            'end_year': experience.end_year,
            'current': experience.current,
            'include_in_resume': True,
            'title': experience.title,
            'short_title': experience.short_title,
            'description': experience.description,
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
    }
