from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
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
    # Show only the current user's foods when authenticated
    if request.user.is_authenticated:
        foods = Food.objects.filter(user=request.user).order_by('-date')
    else:
        foods = Food.objects.none()

    return render(request, 'food_list.html', {'foods': foods})

def food_create(request):
    # Only authenticated users may create food entries
    if not request.user.is_authenticated:
        return redirect('food_diary')

    form = FoodForm(request.POST or None)
    if form.is_valid():
        food = form.save(commit=False)
        food.user = request.user
        food.save()
        messages.success(request, 'Food added successfully.')
        return redirect('food_list')

    return render(request, 'food_form.html', {'form': form})

def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    # Only allow the owner to update
    if not request.user.is_authenticated or food.user != request.user:
        raise Http404

    form = FoodForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        messages.success(request, 'Food updated successfully.')
        return redirect('food_list')

    return render(request, 'food_form.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    # Only allow the owner to delete
    if not request.user.is_authenticated or food.user != request.user:
        raise Http404

    if request.method == "POST":
        food.delete()
        messages.success(request, 'Food deleted.')
        return redirect('food_list')

    return render(request, 'food_delete_confirm.html', {'object': food})




