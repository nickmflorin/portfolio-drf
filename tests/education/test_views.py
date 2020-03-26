import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_education, create_project,
        create_skill, create_course):
    education = create_education()
    courses = [
        create_course(education=education),
        create_course(education=education)
    ]
    projects = [
        create_project(content_object=education),
        create_project(content_object=education)
    ]
    skill = create_skill()
    skill.educations.set([education])

    response = api_client.get('/api/v1/education/')
    assert response.json() == [{
        'id': education.pk,
        'start_month': education.start_month,
        'end_month': education.end_month,
        'start_year': education.start_year,
        'end_year': education.end_year,
        'current': education.current,
        'school': {
            'id': education.school.pk,
            'name': education.school.name,
            'city': education.school.city,
            'state': education.school.state,
            'logo': None,
            'description': education.school.description,
        },
        'degree': education.degree,
        'major': education.major,
        'gpa': education.gpa,
        'minor': education.minor,
        'concentration': education.concentration,
        'description': education.description,
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
                'description': projects[0].description,
            },
            {
                'id': projects[1].pk,
                'name': projects[1].name,
                'description': projects[1].description,
            }
        ]
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
        create_project(content_object=education),
        create_project(content_object=education)
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
        'school': {
            'id': education.school.pk,
            'name': education.school.name,
            'city': education.school.city,
            'state': education.school.state,
            'logo': None,
            'description': education.school.description,
        },
        'degree': education.degree,
        'major': education.major,
        'gpa': education.gpa,
        'minor': education.minor,
        'concentration': education.concentration,
        'description': education.description,
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
                'description': projects[0].description,
            },
            {
                'id': projects[1].pk,
                'name': projects[1].name,
                'description': projects[1].description,
            }
        ]
    }
