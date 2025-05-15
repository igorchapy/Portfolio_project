from django.contrib import admin
from .models import DishType, Cook, Dish, Ingredient

admin.site.register(DishType)
admin.site.register(Cook)
admin.site.register(Dish)
admin.site.register(Ingredient)
