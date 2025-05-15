from django.urls import path
from .views import (
    HomeView,
    AboutCompanyView,
    DishListView,
    DeleteDishView,
    IngredientListView,
    DeleteIngredientView,
    ChefListView,
    AddDishView
)

app_name = 'kitchen_structure'

urlpatterns = [
    path('', HomeView.as_view(), name='head_page'),  # Головна сторінка
    path('about/', AboutCompanyView.as_view(), name='about_company'),  # Сторінка "Про компанію"
    path('dishes/', DishListView.as_view(), name='dishes_view'),  # Сторінка страв
    path('dish/delete/<int:pk>/', DeleteDishView.as_view(), name='delete_dish'),  # Видалення страви
    path('add/', AddDishView.as_view(), name='add_dish'),  # Додавання страви вручну
    path('ingredients/', IngredientListView.as_view(), name='ingredients_view'),  # Інгредієнти
    path('ingredients/delete/<int:pk>/', DeleteIngredientView.as_view(), name='delete_ingredient'),  # Видалення інгредієнта
    path('chefs/', ChefListView.as_view(), name='chefs_list'),  # Список кухарів
]
