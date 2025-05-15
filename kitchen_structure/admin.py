from django.contrib import admin
from .models import DishType, Cook, Ingredient, Dish


@admin.register(DishType)
class DishTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
@admin.register(Cook)
class CookAdmin(admin.ModelAdmin):
    list_display = ('get_name', 'get_email', 'get_phone')

    def get_name(self, obj):
        return obj.user.get_full_name()  # або obj.user.username, якщо не використовуєте ім'я + прізвище
    get_name.short_description = 'Name'

    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

    def get_phone(self, obj):
        return obj.user.phone  # якщо у CustomUser є поле phone
    get_phone.short_description = 'Phone'

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'dish_type', 'get_cooks')
    list_filter = ('dish_type',)
    search_fields = ('name',)

    def get_cooks(self, obj):
        return ", ".join([cook.name for cook in obj.cooks.all()])
    get_cooks.short_description = 'Cooks'
