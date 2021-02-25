from django.db import models

from common.models import Model as DBModel


class Game(DBModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='games')

    @property
    def user_email(self):
        return self.user.email
