from django import forms

from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        # Do not expose the owner in the form; set it server-side in views
        fields = ['name', 'date', 'meal_type']
        widgets = {
            'date': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'meal_type': forms.Select(attrs={'class': 'form-select'}),
        }
