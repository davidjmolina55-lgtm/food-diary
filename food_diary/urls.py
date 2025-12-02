from . import views
from django.urls import include, path

urlpatterns = [
    path('food_diary/', views.food_diary_view, name='food_diary'),
    
]
