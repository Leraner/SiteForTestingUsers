import pytz

from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from exam.serializer import ExamSerializer
from post.models import Post, Category
from users.serializer import CustomUserSerializer
from datetime import datetime


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = CustomUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    tags = TagListSerializerField()
    exam = ExamSerializer(read_only=True)
    created_date = serializers.SerializerMethodField()

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
            'exam',
            'tags',
        ]

    def get_created_date(self, obj):
        now = datetime.now(tz=pytz.UTC)
        date_delta = now - obj.created_date

        days = date_delta.days
        hours = date_delta.seconds // 60 // 60
        minutes = date_delta.seconds // 60
        seconds = date_delta.seconds

        if days != 0 and days < 7:
            return f'{days} days ago' if days != 1 else f'{days} day ago'
        elif minutes > 60:
            return f'{hours} hours ago' if hours != 1 else f'{hours} hour ago'
        elif minutes != 0:
            return f'{minutes} minutes ago' if minutes != 1 else f'{minutes} minute ago'
        elif seconds < 60:
            return f'{seconds} seconds ago' if seconds != 1 else f'{seconds} second ago'
        else:
            return obj.created_date.strftime("%m/%d/%Y")
