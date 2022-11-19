from rest_framework.serializers import ModelSerializer

from questions.models import Question


class QuestionSerializer(ModelSerializer):
    """Question serializer"""

    class Meta:
        model = Question
        fields = [
            'id',
            'question_text',
            'author',
        ]
