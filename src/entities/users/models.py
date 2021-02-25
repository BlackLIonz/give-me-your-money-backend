from django.db import models

from common.models import AbstractUser


class User(AbstractUser):
    balance = models.PositiveIntegerField(default=1000)

    class Meta:
        ordering = (
            '-created_at',
        )
