from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect, get_object_or_404
from .models import Food
from .forms import FoodForm

# Create your views here.
def food_diary_view(request):
    # Render the main diary login/home template
    # Use the Django shortcut `render` which returns an HttpResponse
    # If the user is already logged in, send them straight to the foods list
    if request.user.is_authenticated:
        return redirect('food_list')

    return render(request, 'food_diary.html')
   
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'food_list.html', {'foods': foods})

def food_create(request):
    form = FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food_list')
    return render(request, 'food_form.html', {'form': form})

def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    form = FoodForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        return redirect('food_list')
    return render(request, 'food_form.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('food_list')
    return render(request, 'food_confirm_delete.html', {'food': food})




