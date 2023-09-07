from django.dispatch import receiver
from django.db.models import signals
from TestingUsers.celery import exam_post_cover


@receiver(signals.post_save, sender='post.Post')
def my_callback(sender, instance, created, **kwargs):
    if created:
        return exam_post_cover.delay(instance.id)
