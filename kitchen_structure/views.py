from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .models import Dish, Cook, Ingredient, DishType
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest
from .forms import DishForm


User = get_user_model()

# --- Головна сторінка ---
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'includes/kitchen_structure/head_page.html', {'dishes': dishes})


# --- Сторінка страв ---
def dishes_view(request):
    dishes = Dish.objects.all()
    dish_types = DishType.objects.all()

    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitchen_structure:dishes_view')
    else:
        form = DishForm()

    context = {
        'form': form,
        'dishes': dishes,
        'dish_types': dish_types,
    }
    return render(request, 'includes/kitchen_structure/dishes_view.html', context)


# --- Видалення страви ---
def delete_dish(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    if request.method == 'POST':
        dish.delete()
        return redirect('kitchen_structure:dishes_view')
    return render(request, 'includes/kitchen_structure/delete_dish.html', {'dish': dish})


# --- Сторінка кухарів ---
def chef_list(request):
    chefs = User.objects.filter(is_superuser=True)
    context = {
        'chefs': chefs,
        'chefs_message': None if chefs.exists() else 'Немає суперкухарів для відображення.'
    }
    return render(request, 'includes/kitchen_structure/chefs_list.html', context)


# --- Сторінка "Про компанію" ---
def about_view(request):
    return render(request, 'includes/kitchen_structure/about_company.html')


# --- Інгредієнти ---
@csrf_exempt
def ingredients_view(request: HttpRequest):
    if request.method == 'POST':
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        if name and quantity:
            Ingredient.objects.create(name=name, quantity=quantity)
        return redirect('kitchen_structure:ingredients_view')

    ingredients = Ingredient.objects.all()
    return render(request, 'includes/kitchen_structure/ingredients_view.html', {'ingredients': ingredients})


@csrf_exempt
def delete_ingredient(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('kitchen_structure:ingredients_view')
    return render(request, 'includes/kitchen_structure/delete_ingredient.html', {'ingredient': ingredient})

def add_dish(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        dish_type_name = request.POST.get('dish_type')
        description = request.POST.get('description')
        recipe = request.POST.get('recipe')

        if not (name and dish_type_name and description and recipe):
            # Повертаємо з помилкою, якщо щось не заповнено
            return render(request, 'includes/kitchen_structure/dishes_view.html', {
                'dishes': Dish.objects.all(),
                'dish_types': DishType.objects.all(),
                'error': 'Будь ласка, заповніть усі поля.'
            })

        # Отримуємо або створюємо DishType
        dish_type, created = DishType.objects.get_or_create(name=dish_type_name)

        # Створюємо страву
        Dish.objects.create(
            name=name,
            dish_type=dish_type,
            description=description,
            recipe=recipe
        )

        return redirect('kitchen_structure:dishes')

    # Якщо GET — перенаправляємо
    return redirect('kitchen_structure:dishes')
