from django.shortcuts import render
from .models import Pizza

def index(request):
    """The page for pizzeria"""
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show all pizzas"""
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show a single pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    context = {'pizza': pizza}
    return render(request, 'pizzas/pizza.html', context)
