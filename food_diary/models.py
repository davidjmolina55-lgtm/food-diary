from django.db import models
from django.conf import settings


class Food(models.Model):
    MEAL_TYPES = [
        ("breakfast", "Breakfast"),
        ("lunch", "Lunch"),
        ("dinner", "Dinner"),
        ("snack", "Snack"),
    ]

    name = models.CharField(max_length=100)
    # Automatically set the date when a Food is first created
    date = models.DateField(auto_now_add=True)
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # Optional flag to mark entries as reviewed in the admin
    reviewed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.meal_type})"
