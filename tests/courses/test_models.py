import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_education, create_course):
    education = create_education()
    courses = [
        create_course(education=education),
        create_course(education=education)
    ]
    response = api_client.get('/api/v1/courses/')
