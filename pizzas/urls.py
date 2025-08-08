"""Define URL patterns for pizzas app."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
    #Pizzas page
    path('pizzas/', views.pizzas, name='pizzas'),
    #Single pizza page
    path('pizzas/<int:pizza_id>/', views.pizza, name='pizza'),
]