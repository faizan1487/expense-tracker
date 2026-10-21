from django.db import models
from users.models import User, Team

# Create your models here.
class Expense(models.Model):
    class Categories(models.TextChoices):
        FIXED_EXPENSE = 'FE', 'Fixed Expense'
        RECURRING_EXPENSE = 'RE', 'Recurring Expense'

    name = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.IntegerField()
    category = models.CharField(
        max_length=2,
        choices=Categories.choices,
        default=Categories.FIXED_EXPENSE,
    )
    created_at = models.DateField()
