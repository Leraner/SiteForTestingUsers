import pytest
from django.urls import reverse
from rest_framework import status
from answers.models import Answer

pytestmark = [
    pytest.mark.django_db,
]


# GET(+) POST(+) PUT PATCH
# Question -> Answer

def test_get_answers_without_permissions(api_client, create_user, create_question, create_answer):
    user = create_user
    api_client.force_authenticate(user=user)

    url = reverse('answers-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.parametrize('is_staff', [True])
def test_get_answers(api_client, create_user, create_question, create_answer):
    user = create_user
    api_client.force_authenticate(user=user)

    url = reverse('answers-list')
    response = api_client.get(url)
    print(response)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['results'][0]['answer_text'] == create_answer.answer_text
    assert response.data['results'][0]['question'] == create_answer.id


@pytest.mark.parametrize('is_staff', [True])
def test_create_answer(api_client, create_user, create_question):
    user = create_user
    question = create_question
    api_client.force_authenticate(user=user)

    assert Answer.objects.count() == 0

    data = {
        "answer_text": "TestAnswer",
        "question": question.id
    }
    url = reverse('answers-list')
    response = api_client.post(url, data=data, format='json')

    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['answer_text'] == data['answer_text']
    assert response.data['question'] == data['question']
    assert Answer.objects.count() == 1


@pytest.mark.parametrize('is_staff', [True])
def test_put_answer(api_client, create_user, create_question, create_answer):
    user = create_user
    answer = create_answer

    api_client.force_authenticate(user=user)

    url = reverse('answers-detail', kwargs={'pk': answer.id})
    ...

# TODO: Write this part of code

