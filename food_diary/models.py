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
    date = models.DateField()
    meal_type = models.CharField(max_length=20, choices=MEAL_TYPES)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.meal_type})"
