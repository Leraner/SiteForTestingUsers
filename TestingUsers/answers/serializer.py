from rest_framework import serializers

from answers.models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """Answer serializer"""

    class Meta:
        model = Answer
        fields = [
            'id',
            'answer_text',
            'question',
        ]
