from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateField()


class User(AbstractUser):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    currency = models.CharField(max_length=10, null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
