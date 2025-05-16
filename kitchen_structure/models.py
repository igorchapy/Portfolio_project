from django.db import models
from django.contrib.auth.models import AbstractUser


class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} ({self.quantity})'


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    recipe = models.TextField()
    dish_type = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cook(AbstractUser):
    position = models.CharField(max_length=100)
    age = models.PositiveIntegerField(null=True, blank=True)
    experience = models.PositiveIntegerField(null=True, blank=True)


    def __str__(self):
        return f"{self.get_full_name()} ({self.username})"
