import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_education, create_project,
        create_skill, create_course):
    education = create_education()
    response = api_client.get('/api/v1/education/')
    assert response.json() == [{
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
    }]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_education, create_project,
        create_skill, create_course):
    education = create_education()
    courses = [
        create_course(education=education),
        create_course(education=education)
    ]
    projects = [
        create_project(education=education),
        create_project(education=education)
    ]
    skill = create_skill()
    skill.educations.set([education])

    response = api_client.get('/api/v1/education/%s/' % education.pk)
    assert response.status_code == 200
    assert response.json() == {
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
        'skills': [
            {
                'id': skill.pk,
                'name': skill.name,
            }
        ],
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
