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
        },
        {
            'id': skills[1].pk,
            'name': skills[1].name,
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
        'educations': [{
            'id': education.pk,
            'start_month': education.start_month,
            'end_month': education.end_month,
            'start_year': education.start_year,
            'end_year': education.end_year,
            'current': education.current,
            'degree': education.degree,
            'major': education.major,
            'minor': education.minor,
            'concentration': education.concentration,
            'description': education.description,
            'gpa': education.gpa,
            'school': {
                'id': education.school.pk,
                'name': education.school.name,
                'city': education.school.city,
                'state': education.school.state,
                'logo': None,
                'description': education.school.description,
            },
        }],
        'projects': [{
            'id': project.id,
            'name': project.name,
            'short_description': project.short_description,
        }],
        'courses': [
            {
                'id': courses[0].pk,
                'name': courses[0].name,
                'description': courses[0].description,
            },
            {
                'id': courses[1].pk,
                'name': courses[1].name,
                'description': courses[1].description,
            }
        ],
        'experiences': [{
            'id': experience.pk,
            'start_month': experience.start_month,
            'end_month': experience.end_month,
            'start_year': experience.start_year,
            'end_year': experience.end_year,
            'current': experience.current,
            'title': experience.title,
            'description': experience.description,
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
    }
