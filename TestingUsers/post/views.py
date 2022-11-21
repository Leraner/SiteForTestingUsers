from django.core.files.images import ImageFile
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.services import resize_image, crop_image, prepare_image_coordinates
from .serializers import PostSerializer, CategorySerializer
from .models import PostEnumChoice, Category, Post
from .permissions import IsAuthOrReadOnly


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_class = IsAuthenticated

    def get_queryset(self):
        return Category.objects.all()


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_class = IsAuthOrReadOnly

    def get_queryset(self):
        return Post.objects.filter(status=PostEnumChoice.RELEASE).order_by('-created_date')

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        cover = data.pop('cover')

        # check for erotic photos

        category = Category.objects.filter(
            slug=data.pop('category')).first()

        if category is not None:
            data['category'] = category.title

        if cover:
            image = cover.get('image')
            coords = cover.get('coords')

            b_image = crop_image(
                image, prepare_image_coordinates(coords))

            cover = ImageFile(b_image[0], name=f'{request.user.pk}.jpeg')
            data['cover'] = cover

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)
