from uuid import uuid4

from django.db import models as django_db_models
from django.contrib.auth.models import AbstractUser as _AbstractUser


class Model(django_db_models.Model):
    id = django_db_models.UUIDField(primary_key=True, db_index=True, default=uuid4, editable=False)
    created_at = django_db_models.DateTimeField(auto_now_add=True)
    updated_at = django_db_models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AbstractUser(_AbstractUser):
    id = django_db_models.UUIDField(primary_key=True, db_index=True, default=uuid4, editable=False)
    created_at = django_db_models.DateTimeField(auto_now_add=True)
    updated_at = django_db_models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
