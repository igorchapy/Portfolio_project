from django import forms
from .models import Dish, Ingredient, Cook


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = "__all__"

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ["name"]
class CookForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["username", "first_name", "last_name"]

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'dish_type', 'cooks', 'ingredients']
