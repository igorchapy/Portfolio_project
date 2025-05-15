from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class DishType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cook(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.get_full_name() or self.username


class Dish(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField("Cook")
    ingredients = models.ManyToManyField("Ingredient", blank=True)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)  # quantity in grams, cups, etc.

    def __str__(self):
        return self.name
