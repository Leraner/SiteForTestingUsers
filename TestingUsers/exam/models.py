from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class ExamQuestion(models.Model):
    """Exam's question"""
    question_text = models.CharField(max_length=100)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='exam_questions_author'
    )

    def __str__(self):
        return self.question_text


class ExamAnswer(models.Model):
    """Exam question's answer"""
    answer_text = models.CharField(max_length=100)
    question = models.OneToOneField(
        ExamQuestion,
        on_delete=models.CASCADE,
        related_name='exam_answer'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='exam_answer_author'
    )

    def __str__(self):
        return self.answer_text


class Exam(models.Model):
    """Exam model"""
    title = models.CharField(max_length=100, default='No name test')
    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='exam_author'
    )
    questions = models.ManyToManyField(ExamQuestion)

    def __str__(self):
        return f'Exam: {self.author.username} (ID {self.author.id})'
