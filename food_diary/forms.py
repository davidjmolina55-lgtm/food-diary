from django import forms

from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['name', 'date', 'meal_type', 'user']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'meal_type': forms.Select(attrs={'class': 'form-select'}),
            'user': forms.Select(attrs={'class': 'form-select'}),
        }
