from django.dispatch import receiver
from djoser.signals import user_registered
from TestingUsers.celery import send_registration_email


@receiver(user_registered)
def send_user_email(**kwargs):
    user = kwargs['user']
    return send_registration_email.delay(username=user.username, email=user.email)


# TODO: add it when we will it on the production
