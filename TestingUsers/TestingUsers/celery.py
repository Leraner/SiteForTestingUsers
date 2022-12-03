"""
Celery config file

https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html

"""
from __future__ import absolute_import

import os

from celery import Celery
from celery import shared_task
from django.apps import apps
from django.conf import settings
from django.core.mail import send_mail

# this code copied from manage.py
# set the default Django settings module for the 'celery' app.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestingUsers.settings')

app = Celery("TestingUsers")

# read config from Django settings, the CELERY namespace would make celery
# config keys has `CELERY` prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# load tasks.py in django apps
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task
def send_registration_email(username, email):
    context = {
        'username': username,
        'email': email,
    }

    return send_mail(
        subject='Hello user',
        message=f'Test message for user: {context["username"]} - username, this is test email after registration',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[context["email"]]
    )


@shared_task()
def exam_post_cover(instance_pk):
    import opennsfw2 as n2
    from post.models import PostEnumChoice

    post = apps.get_model('post', 'Post')
    post = post.objects.get(id=instance_pk)

    nsfw_probability = n2.predict_image(post.cover.path)
    is_not_nsfw_content = True if nsfw_probability < 0.10 else False

    if is_not_nsfw_content:
        post.status = PostEnumChoice.RELEASE
        post.save()

    return 'Post has been released' if is_not_nsfw_content else 'Post on moderation'
