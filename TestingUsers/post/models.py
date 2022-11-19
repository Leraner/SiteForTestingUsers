from enum import Enum
from glob import glob
from random import randint

from django.db import models
from django_enum_choices.fields import EnumChoiceField
from taggit.managers import TaggableManager

from exam.models import Exam
from users.models import CustomUser


class PostEnumChoice(Enum):
    RELEASE = 'release'
    MODERATION = 'moderation'


class Category(models.Model):
    title = models.CharField(unique=True, max_length=20)
    slug = models.SlugField(unique=True, max_length=5)

    def __str__(self):
        return self.title


def set_default_category():
    return Category.objects.filter(slug='other').first()


def set_random_default_cover():
    covers = glob('media/post_cover/default_post_covers/*.jpeg')
    return covers[randint(0, len(covers) - 1)].replace('media/', '')


class Post(models.Model):
    title = models.CharField(max_length=100)
    cover = models.ImageField(blank=True, null=True,
                              default=set_random_default_cover,
                              upload_to="post_cover/%Y/%m/%d/")
    body = models.TextField()
    status = EnumChoiceField(PostEnumChoice, default=PostEnumChoice.MODERATION)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='post_author'
    )
    category = models.ForeignKey(
        Category,
        default=set_default_category,
        on_delete=models.CASCADE,
        related_name='post_category'
    )
    exams = models.ForeignKey(
        Exam,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='post_exam'
    )
    created_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f'Post {self.author.username} ({self.author.id})'

    def delete(self, *args, **kwargs):
        if self.cover:
            self.cover.delete()
        super().delete(*args, **kwargs)
