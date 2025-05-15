from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from .models import Dish, DishType, Cook, Ingredient
from django.contrib.auth.models import User
from .forms import DishForm


# Головна сторінка
def home(request):
    return HttpResponse("Welcome to the Kitchen App!")


# Створення та відображення списку страв
def dish_list_and_create(request):
    # Отримуємо страви та типи страв з бази даних
    dishes = Dish.objects.all()
    dish_types = DishType.objects.all()
    selected_type_id = request.GET.get('dish_type')  # Отримуємо вибраний тип страви з параметрів запиту

    # Обробка форми при POST-запиті
    if request.method == 'POST':
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitchen:dish-list')  # Перенаправлення на список страв після збереження
    else:
        form = DishForm()

    # Повертаємо шаблон з контекстом
    context = {
        'dishes': dishes,
        'form': form,
        'dish_types': dish_types,
        'selected_type_id': selected_type_id
    }

    return render(request, 'kithen/dish_list_and_create.html', context)

# Список страв
class DishListView(ListView):
    model = Dish
    template_name = 'kithen_structure/dish_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DishForm()  # Додаємо форму на список страв
        return context

    def post(self, request, *args, **kwargs):
        form = DishForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kitchen:dish-list')  # Перенаправляємо на список страв
        context = self.get_context_data()
        context["form"] = form  # Додаємо помилки форми, якщо вона не валідна
        return self.render_to_response(context)


# Страва: Деталі
class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    template_name = "kithen_structure/dish_detail.html"


# Страва: Створення
class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kithen_structure/dish_form.html"


# Страва: Оновлення
class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kithen_structure/dish_form.html"


# Страва: Видалення
class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("kitchen:dish-list")
    template_name = "kithen_structure/dish_confirm_delete.html"


# Список типів страв
class DishTypeListView(LoginRequiredMixin, generic.ListView):
    model = DishType
    template_name = "kithen_structure/dishtype_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['additional_data'] = 'some value'  # Приклад додавання додаткових даних
        return context


# Створення типу страви
class DishTypeCreateView(LoginRequiredMixin, generic.CreateView):
    model = DishType
    fields = "__all__"
    success_url = reverse_lazy("kitchen:dishtype-list")
    template_name = "kithen_structure/dishtype_form.html"


# Список кухарів
class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    template_name = "kithen_structure/cook_list.html"


# Деталі кухаря
class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    template_name = "kithen_structure/cook_detail.html"


# Список користувачів
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'kithen_structure/user_list.html'
    context_object_name = 'users'


# Деталі користувача
class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'kithen_structure/user_detail.html'
    context_object_name = 'user'


# Створення інгредієнта
class IngredientCreateView(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    fields = "__all__"
    success_url = reverse_lazy("kitchen:ingredient-list")
    template_name = "kithen_structure/ingredient_form.html"


# Список інгредієнтів
class IngredientListView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "kithen_structure/ingredient_list.html"
    context_object_name = "object_list"  # Це ім'я змінної, яку використовує шаблон
