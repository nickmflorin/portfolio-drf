import pytest

from portfolio.app.comments.models import Comment


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
            'comment': comments[0].comment,
            'public': comments[0].public,
            'date_modified': comments[0].date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': comments[0].date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
        },
        {
            'id': comments[1].pk,
            'name': comments[1].name,
            'email': comments[1].email,
            'comment': comments[1].comment,
            'public': comments[1].public,
            'date_modified': comments[1].date_modified.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
            'date_created': comments[1].date_created.strftime(
                "%Y-%m-%dT%H:%M:%S.%fZ"),
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
        'comment': comment.comment,
        'public': comment.public,
        'date_modified': comment.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': comment.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
    }


@pytest.mark.django_db
def test_create_comment(api_client):
    data = {
        'name': 'Comment Author',
        'comment': 'Some Comment',
        'email': 'author@gmail.com',
        'public': False,
    }
    response = api_client.post('/api/v1/comments/', data=data)
    assert response.status_code == 201

    comment = Comment.objects.first()
    assert response.json() == {
        'id': comment.pk,
        'date_modified': comment.date_modified.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'date_created': comment.date_created.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),
        'comment': 'Some Comment',
        'public': False,
        'email': 'author@gmail.com',
        'name': 'Comment Author',
    }


@pytest.mark.django_db
def test_update_comment(api_client, create_comment):
    data = {'name': 'New Name'}
    comment = create_comment()
    response = api_client.post('/api/v1/comments/%s/' % comment.pk, data=data)
    assert response.status_code == 405


@pytest.mark.django_db
def test_delete_comment(api_client, create_comment):
    comment = create_comment()
    response = api_client.delete('/api/v1/comments/%s/' % comment.pk)
    assert response.status_code == 405
