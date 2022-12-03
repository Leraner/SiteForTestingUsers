import time

from django.contrib.auth.models import AbstractUser
from django.db import models


def user_upload_to_path_avatar(instance, tmp_image_name):
    filename = str(instance.id) + f"__{time.time()}.jpeg"
    date = time.strftime("%Y/%m/%d", time.localtime())
    return f'profile/avatar/{date}/{filename}'


class CustomUser(AbstractUser):
    status = models.CharField('Status', max_length=20)
    right_answers = models.IntegerField(default=0)
    all_answers = models.IntegerField(default=0)
    user_avatar = models.ImageField(
        default='default_user_avatar.png',
        upload_to=user_upload_to_path_avatar,
        verbose_name='UserAvatar'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.pk}: {self.username}'
