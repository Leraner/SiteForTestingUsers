import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status

User = get_user_model()

pytestmark = [
    pytest.mark.django_db,
]


def test_get_user_list(api_client, create_user) -> None:
    url = reverse('users-list')
    user = create_user

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data[0]['username'] == user.username
    assert response.data[0]['id'] == user.id
    assert response.data[0]['email'] == user.email


def test_user_create(api_client) -> None:
    user_data = {
        'username': 'Testusername',
        'password': 'testpassword123',
        'email': 'testemail@gmail.com',
        'status': 'teststatus'
    }

    assert User.objects.count() == 0

    url = reverse('customuser-list')

    response = api_client.post(url, user_data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.count() == 1

    user = User.objects.filter(id=response.data['id']).first()

    assert user is not None
    assert user.username == user_data['username']
    assert user.password is not None


def test_user_update(api_client, create_user):
    user = create_user
    api_client.force_authenticate(user=user)

    new_user_data = {
        'username': 'Testusername1',
        'password': 'testpassword1231',
        'email': 'testemail1@gmail.com',
        'status': 'teststatus',
        'right_answers': user.right_answers + 1,
        'all_answers': user.all_answers + 1
    }

    url = reverse('users-detail', kwargs={'username': user.username})
    response = api_client.put(url, data=new_user_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == new_user_data['username']
    assert response.data['email'] == new_user_data['email']
    assert response.data['status'] == new_user_data['status']
    assert response.data['right_answers'] == new_user_data['right_answers']
    assert response.data['all_answers'] == new_user_data['all_answers']


def test_user_patch(api_client, create_user):
    user = create_user
    api_client.force_authenticate(user=user)

    new_user_data = {
        'username': 'Testusername1',
        'password': 'testpassword1231',
        'email': 'testemail1@gmail.com'
    }

    url = reverse('users-detail', kwargs={'username': user.username})

    response = api_client.patch(url, data=new_user_data, format='json')

    assert response.status_code == status.HTTP_200_OK
    assert response.data['username'] == new_user_data['username']
    assert response.data['email'] == new_user_data['email']
    assert response.data['status'] == user.status
