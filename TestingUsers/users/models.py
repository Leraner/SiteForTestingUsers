from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    status = models.CharField('Status', max_length=20)
