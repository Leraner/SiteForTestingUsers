from django.contrib.auth import get_user_model
from django.db import models

from questions.models import Question

User = get_user_model()


class Answer(models.Model):
    """Answer model"""
    answer_text = models.CharField(max_length=100)
    question = models.OneToOneField(
        Question,
        on_delete=models.CASCADE,
        related_name='answer'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='answer_author'
    )

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'

    def __str__(self):
        return self.answer_text
