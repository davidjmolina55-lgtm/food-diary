from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.food_diary_view, name='food_diary'),
]
