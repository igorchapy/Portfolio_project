from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .models import Dish, Cook, Ingredient, DishType
from .forms import DishForm

User = get_user_model()


# --- Головна сторінка ---
class HomeView(ListView):
    model = Dish
    template_name = 'includes/kitchen_structure/head_page.html'
    context_object_name = 'dishes'


# --- Сторінка страв ---
class DishListView(View):
    def get(self, request):
        dishes = Dish.objects.all()
        dish_types = DishType.objects.all()
        form = DishForm()
        return render(request, 'includes/kitchen_structure/dishes_view.html', {
            'form': form,
            'dishes': dishes,
            'dish_types': dish_types,
        })

    def post(self, request):
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitchen_structure:dishes_view')

        dishes = Dish.objects.all()
        dish_types = DishType.objects.all()
        return render(request, 'includes/kitchen_structure/dishes_view.html', {
            'form': form,
            'dishes': dishes,
            'dish_types': dish_types,
        })


# --- Додавання страви через просту форму ---
class AddDishView(View):
    def post(self, request):
        name = request.POST.get('name')
        dish_type_name = request.POST.get('dish_type')
        description = request.POST.get('description')
        recipe = request.POST.get('recipe')

        if not (name and dish_type_name and description and recipe):
            return render(request, 'includes/kitchen_structure/dishes_view.html', {
                'dishes': Dish.objects.all(),
                'dish_types': DishType.objects.all(),
                'error': 'Будь ласка, заповніть усі поля.'
            })

        dish_type, _ = DishType.objects.get_or_create(name=dish_type_name)
        Dish.objects.create(
            name=name,
            dish_type=dish_type,
            description=description,
            recipe=recipe
        )
        return redirect('kitchen_structure:dishes')

    def get(self, request):
        return redirect('kitchen_structure:dishes')


# --- Видалення страви ---
class DeleteDishView(DeleteView):
    model = Dish
    template_name = 'includes/kitchen_structure/delete_dish.html'
    success_url = reverse_lazy('kitchen_structure:dishes_view')
    context_object_name = 'dish'


# --- Сторінка кухарів ---
class ChefListView(ListView):
    model = User
    template_name = 'includes/kitchen_structure/chefs_list.html'
    context_object_name = 'chefs'

    def get_queryset(self):
        return User.objects.filter(is_superuser=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if not context['chefs'].exists():
            context['chefs_message'] = 'Немає суперкухарів для відображення.'
        return context


# --- Сторінка "Про компанію" ---
class AboutCompanyView(TemplateView):
    template_name = 'includes/kitchen_structure/about_company.html'


# --- Інгредієнти ---
class IngredientListView(View):
    def get(self, request):
        ingredients = Ingredient.objects.all()
        return render(request, 'includes/kitchen_structure/ingredients_view.html', {'ingredients': ingredients})

    def post(self, request):
        name = request.POST.get('name')
        quantity = request.POST.get('quantity')
        if name and quantity:
            Ingredient.objects.create(name=name, quantity=quantity)
        return redirect('kitchen_structure:ingredients_view')


class DeleteIngredientView(View):
    def get(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        return render(request, 'includes/kitchen_structure/delete_ingredient.html', {'ingredient': ingredient})

    def post(self, request, pk):
        ingredient = get_object_or_404(Ingredient, pk=pk)
        ingredient.delete()
        return redirect('kitchen_structure:ingredients_view')
