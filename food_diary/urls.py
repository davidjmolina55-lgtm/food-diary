from django.urls import path, include
from allauth.account.views import LoginView as AllauthLoginView
from . import views

urlpatterns = [
    # Route the site root to allauth's LoginView using our home template.
    # This lets failed logins redisplay on the home page with errors.
    path(
        '',
        AllauthLoginView.as_view(
            template_name='food_diary.html',
        ),
        name='food_diary',
    ),
    path("accounts/", include("allauth.urls")),
    path('food_diary/', views.food_diary_view, name='food_diary_page'),
    path('foods/', views.food_list, name='food_list'),
    path('create/', views.food_create, name='food_create'),
    path('update/<int:pk>/', views.food_update, name='food_update'),
    path('delete/<int:pk>/', views.food_delete, name='food_delete'),
]
