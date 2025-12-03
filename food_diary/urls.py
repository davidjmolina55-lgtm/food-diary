from . import views
from django.urls import path

urlpatterns = [
    # Make the diary view available at both the site root and /food_diary/
    path('', views.food_diary_view, name='food_diary'),
    path('food_diary/', views.food_diary_view, name='food_diary_page'),
    path('foods/', views.food_list, name='food_list'),
    path('create/', views.food_create, name='food_create'),
    path('update/<int:pk>/', views.food_update, name='food_update'),
    path('delete/<int:pk>/', views.food_delete, name='food_delete'),
]
