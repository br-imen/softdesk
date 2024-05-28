from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    age = models.IntegerField()
    can_be_contacted = models.BooleanField(default=False)
    can_data_be_shared = models.BooleanField(default=False)
    password = models.CharField(max_length=128)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["age", "password"]
