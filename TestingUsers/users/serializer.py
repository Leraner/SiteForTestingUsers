from rest_framework.serializers import ModelSerializer
from users.models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'status', 'id', 'email']
