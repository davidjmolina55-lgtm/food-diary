from django import forms

from .models import Food


class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        # Do not expose the owner in the form; set it server-side in views
        # Expose only editable fields; `date` is set automatically.
        fields = ['name', 'meal_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'meal_type': forms.Select(attrs={'class': 'form-select'}),
        }
