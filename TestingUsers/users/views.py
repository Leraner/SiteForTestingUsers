from rest_framework.viewsets import ModelViewSet

from users.models import CustomUser
from users.serializer import CustomUserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return CustomUser.objects.all()
