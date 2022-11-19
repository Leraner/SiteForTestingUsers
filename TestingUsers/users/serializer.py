from rest_framework.serializers import ModelSerializer, SerializerMethodField
from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    exam_count = SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'username',
            'status',
            'user_avatar',
            'id',
            'email',
            'right_answers',
            'all_answers',
            'exam_count',
        ]

    def get_exam_count(self, user):
        return user.exam_author.count()
