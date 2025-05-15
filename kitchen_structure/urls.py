from django.urls import path
from . import views


app_name = 'kitchen_structure'

urlpatterns = [
    path('', views.home, name='head_page'),  # Головна сторінка
    path('about/', views.about_view, name='about_company'),  # Сторінка "Про компанію"
    path('dishes/', views.dishes_view, name='dishes_view'),  # Страви
    path('dish/delete/<int:dish_id>/', views.delete_dish, name='delete_dish'),
    path('ingredients/', views.ingredients_view, name='ingredients_view'),  # Інгредієнти
    path('chefs/', views.chef_list, name='chefs_list'),  # Кухарі
    path('ingredients/delete/<int:pk>/', views.delete_ingredient, name='delete_ingredient'),
    path('add/', views.add_dish, name='add_dish'),
]
