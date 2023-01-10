from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    """
    This is a custom auth user model
    """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
