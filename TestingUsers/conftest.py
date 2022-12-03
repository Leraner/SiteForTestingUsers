import pytest
from TestingUsers import settings
from rest_framework.test import APIClient

from answers.models import Answer
from questions.models import Question
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.fixture(autouse=True)
def override_settings():
    settings.CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }


@pytest.fixture(scope='function')
def api_client():
    return APIClient()


@pytest.fixture(scope='function')
def is_staff():
    return False


@pytest.fixture(scope='function')
def user_data(is_staff):
    return {
        'username': 'Testusername',
        'password': 'testpassword123',
        'email': 'testemail@gmail.com',
        'is_staff': is_staff
    }


@pytest.fixture(scope='function')
def create_user(user_data):
    return User.objects.create_user(**user_data)


@pytest.fixture(scope='function')
def create_question():
    return Question.objects.create(question_text='TestQuestionText')


@pytest.fixture(scope='function')
def create_answer():
    question = Question.objects.filter(question_text='TestQuestionText').first()
    return Answer.objects.create(answer_text='TestAnswer', question=question)
