from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from exam.serializer import ExamSerializer
from post.models import Post, Category
from users.serializer import CustomUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()
    exams = ExamSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'cover',
            'body',
            'author',
            'category',
            'created_date',
            'exams',
            'tags',
        ]

    def create(self, validated_data):
        return Post.objects.create(author=self.context['request'].user, **validated_data)
