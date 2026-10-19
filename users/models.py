from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Team(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateField()
