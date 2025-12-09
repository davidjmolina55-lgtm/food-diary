from django import forms

from .models import Food
try:
    from allauth.account.forms import SignupForm, LoginForm
except Exception:
    SignupForm = None
    LoginForm = None


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


if SignupForm is not None:
    class CustomSignupForm(SignupForm):
        """Signup form that adds Bootstrap classes to widgets."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            from django.forms import widgets as form_widgets
            for name, field in self.fields.items():
                widget = field.widget
                existing = widget.attrs.get('class', '')

                if isinstance(widget, form_widgets.CheckboxInput):
                    cls = 'form-check-input'
                elif isinstance(widget, form_widgets.Select):
                    cls = 'form-select'
                else:
                    cls = 'form-control'

                classes = (existing + ' ' + cls).strip()
                widget.attrs['class'] = classes


if LoginForm is not None:
    class CustomLoginForm(LoginForm):
        """Login form that adds Bootstrap classes to widgets."""

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            from django.forms import widgets as form_widgets
            for name, field in self.fields.items():
                widget = field.widget
                existing = widget.attrs.get('class', '')

                if isinstance(widget, form_widgets.CheckboxInput):
                    cls = 'form-check-input'
                elif isinstance(widget, form_widgets.Select):
                    cls = 'form-select'
                else:
                    cls = 'form-control'

                classes = (existing + ' ' + cls).strip()
                widget.attrs['class'] = classes
