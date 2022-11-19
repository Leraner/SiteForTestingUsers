from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Question(models.Model):
    """Question model"""
    question_text = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='questions_author'
    )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return self.question_text
