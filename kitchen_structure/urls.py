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
    path('', HomeView.as_view(), name='head_page'),  # Head page
    path('about/', AboutCompanyView.as_view(), name='about_company'),  # About company
    path('dishes/', DishListView.as_view(), name='dishes_view'),  # dishes_view
    path('dish/delete/<int:pk>/', DeleteDishView.as_view(), name='delete_dish'),  # delete_dish
    path('add/', AddDishView.as_view(), name='add_dish'),  # add_dish
    path('ingredients/', IngredientListView.as_view(), name='ingredients_view'),  # ingredients_view
    path('ingredients/delete/<int:pk>/', DeleteIngredientView.as_view(), name='delete_ingredient'),  # delete_ingredient
    path('chefs/', ChefListView.as_view(), name='chefs_list'),  #  chefs_list
]
