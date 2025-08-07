# Pizzeria_Django
Simple pizzas management in django

Cheatsheet
Preconditions:
1. Create environment ```python -m venv <env_name>```
2. Activate environment and install django to the env: ```pip install django```

Steps:
1. Create project ```django-admin startproject pizzeria .```
2. Make project migrations: ```python manage.py migrate```
3. Create application: ```django-admin startapp pizzas```
4. Add pizzas app to pizzeria/settings.py INSTALLED_APPS list
5. Create models (in pizzas/models.py). For Pizza model:  Name, Description, Price. For Topping: name, pizza (foreign key)
6. Prepare db for migrations: ```python manage.py makemigrations pizzas```
7. Migrate model to db: ```python manage.py migrate```
8. Run local server: ```python manage.py runserver```
9. Create super user: ```python manage.py createsuperuser```
10. Register models in the administrator interface (pizzas/admin.py)
```python
from django.contrib import admin
from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
```

Create home page:
1. Create pizzas/urls.py 
```python
#"""Define URL patterns for pizzas app."""
from django.urls import path
from . import views

app_name = 'pizzas'
urlpatterns = [
    #Home page
    path('', views.index, name='index'),
]
```
2. Add ```python  path('', include('pizzas.urls')),  # Include URLs from the pizzas app ``` to ulrpatterns in pizzeria/urls.py
3. Add method returning render of index.html page in views page 
```python
def index(request):
    """The page for pizzeria"""
    return render(request, 'pizzas/index.html')
    ```
4. Create pizzas/template/index.html file



