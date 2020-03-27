import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_education, create_course, create_skill):
    education = create_education()
    skill = create_skill()
    courses = [
        create_course(education=education),
        create_course(education=education)
    ]
    courses[0].skills.add(skill)
    response = api_client.get('/api/v1/courses/')

    assert response.status_code == 200
    assert response.json() == [
        {
            'id': courses[0].pk,
            'name': courses[0].name,
            'description': courses[0].description,
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
            },
            'skills': [{
                'id': skill.pk,
                'name': skill.name
            }],
        },
        {
            'id': courses[1].pk,
            'name': courses[1].name,
            'description': courses[1].description,
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
            },
            'skills': [],
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_education, create_course, create_skill):
    education = create_education()
    skill = create_skill()
    course = create_course(education=education)
    course.skills.add(skill)

    response = api_client.get('/api/v1/courses/%s/' % course.pk)

    assert response.status_code == 200
    assert response.json() == {
        'id': course.pk,
        'name': course.name,
        'description': course.description,
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
        },
        'skills': [{
            'id': skill.pk,
            'name': skill.name
        }]
    }
