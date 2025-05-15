from django import forms
from .models import Dish, Ingredient, Cook


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]

class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "age",
            "experience",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control", "min": 18}),
            "experience": forms.NumberInput(attrs={"class": "form-control", "min": 0}),
        }
        labels = {
            "username": "Ім’я користувача",
            "first_name": "Ім’я",
            "last_name": "Прізвище",
            "email": "Email",
            "age": "Вік",
            "experience": "Стаж роботи (років)",
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'dish_type', 'description', 'recipe']
