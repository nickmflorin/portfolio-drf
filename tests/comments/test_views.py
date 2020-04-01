import pytest


@pytest.mark.django_db
def test_list_response_200(api_client, create_comment):
    comments = [
        create_comment(),
        create_comment()
    ]
    response = api_client.get('/api/v1/comments/')
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': comments[0].pk,
            'name': comments[0].name,
            'email': comments[0].email,
            'value': comments[0].value,
            'public': comments[0].public,
            'date_modified': comments[0].date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': comments[0].date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        },
        {
            'id': comments[1].pk,
            'name': comments[1].name,
            'email': comments[1].email,
            'value': comments[1].value,
            'public': comments[1].public,
            'date_modified': comments[1].date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': comments[1].date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        }
    ]


@pytest.mark.django_db
def test_detail_response_200(api_client, create_comment):
    comment = create_comment()
    response = api_client.get('/api/v1/comments/%s/' % comment.pk)
    assert response.status_code == 200
    assert response.json() == {
        'id': comment.pk,
        'name': comment.name,
        'email': comment.email,
        'value': comment.value,
        'public': comment.public,
        'date_modified': comment.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': comment.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    }
