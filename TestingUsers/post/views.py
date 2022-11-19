from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
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
        return Post.objects.filter(status=PostEnumChoice.RELEASE)

    def create(self, request, *args, **kwargs):
        category = Category.objects.filter(
            slug=request.data.pop('category')).first()

        if category is not None:
            request.data['category'] = category.slug

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(serializer.data)
