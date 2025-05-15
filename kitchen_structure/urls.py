from django.urls import path
from . import views


app_name = 'kitchen'

urlpatterns = [
    path('', views.DishListView.as_view(), name='dish-list'),
    path('dish/create/', views.DishCreateView.as_view(), name='dish-create'),
    path('dish/<int:pk>/', views.DishDetailView.as_view(), name='dish-detail'),
    path('dish/<int:pk>/update/', views.DishUpdateView.as_view(), name='dish-update'),
    path('dish/<int:pk>/delete/', views.DishDeleteView.as_view(), name='dish-delete'),
    path('dish-types/', views.DishTypeListView.as_view(), name='dishtype-list'),
    path('dish-types/create/', views.DishTypeCreateView.as_view(), name='dishtype-create'),
    path('cooks/', views.CookListView.as_view(), name='cook-list'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient-list'),
    path('ingredient/create/', views.IngredientCreateView.as_view(), name='ingredient-create'),
]
