from django.core.files.images import ImageFile
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import CustomUser
from users.serializer import CustomUserSerializer
from .exceptions import ImageRequiredException
from .exceptions import RefreshTokenNotFoundException
from .services import crop_image, prepare_image_coordinates, resize_image


class CustomUserView(ModelViewSet):
    serializer_class = CustomUserSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]

    lookup_field = 'username'

    def get_queryset(self):
        return CustomUser.objects.all()

    @action(detail=False, methods=['GET'], permission_classes=[IsAuthenticated])
    def profile(self, request):
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def update_user_avatar(self, request):
        image = request.data.get('image')
        coords = request.data.get('coords')

        try:
            if request.user.user_avatar.name in image:
                b_image = resize_image(
                    request.user.user_avatar.name, prepare_image_coordinates(coords))
            else:
                b_image = crop_image(image, prepare_image_coordinates(coords))
        except ImageRequiredException as error:
            return Response({'message': error}, status=status.HTTP_404_NOT_FOUND)

        avatar = ImageFile(b_image[0], name=f'{request.user.pk}.jpeg')
        request.user.user_avatar.delete()
        request.user.user_avatar = avatar
        request.user.save()

        serializer = self.get_serializer(instance=request.user)

        return Response(serializer.data)

    @action(detail=False, methods=['POST'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        """
        Get refresh -> refresh token
        """
        try:
            refresh_token = request.data.get('refresh')
            if not refresh_token:
                raise RefreshTokenNotFoundException()

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(
                {'message': 'Token has been deleted'},
                status=status.HTTP_205_RESET_CONTENT
            )
        except RefreshTokenNotFoundException:

            return Response(
                {'message': 'Token not found'},
                status=status.HTTP_400_BAD_REQUEST
            )
        except TokenError:
            return Response(
                {'message': 'Token already in blacklist'},
                status=status.HTTP_400_BAD_REQUEST
            )
