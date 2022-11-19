from rest_framework import serializers

from users.serializer import CustomUserSerializer
from .models import Exam, ExamAnswer, ExamQuestion


class ExamQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamQuestion
        fields = '__all__'


class ExamAnswerSerializer(serializers.ModelSerializer):
    question = ExamQuestionSerializer(read_only=True)

    class Meta:
        model = ExamAnswer
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    questions = ExamQuestionSerializer(many=True, read_only=True)
    author = CustomUserSerializer(read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'title', 'author', 'questions']
