from django.core.files.images import ImageFile
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from exam.models import Exam
from users.services import crop_image, prepare_image_coordinates
from .models import PostEnumChoice, Category, Post
from .serializers import PostSerializer, CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    permission_class = IsAuthenticated

    def get_queryset(self):
        return Category.objects.all()


# TODO: Post edit
# TODO: Post delete

class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    permission_class = IsAuthenticatedOrReadOnly

    def get_queryset(self):
        return Post.objects.filter(status=PostEnumChoice.RELEASE).order_by('-created_date')

    @action(methods=['GET'], detail=False, permission_classes=[IsAuthenticated])
    def my_posts(self, request):
        queryset = self.get_queryset().filter(author=request.user)
        serializer = PostSerializer(instance=queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        cover = data.pop('cover')

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

    def perform_create(self, serializer):
        if self.request.data.get('exam') == '':
            serializer.validated_data['exam'] = None
        else:
            exam = Exam.objects.filter(id=self.request.data.pop('exam')).first()

            if exam is not None:
                serializer.validated_data['exam'] = exam

        serializer.validated_data['author'] = self.request.user
        serializer.save()
