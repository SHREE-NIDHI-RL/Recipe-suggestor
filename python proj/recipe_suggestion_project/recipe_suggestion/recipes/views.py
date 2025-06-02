from django.shortcuts import render
from .models import Recipe
from django.shortcuts import get_object_or_404
from .models import Recipe

from django.http import JsonResponse
from .models import Recipe
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import  redirect
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')  # Redirect to the homepage after login
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the homepage after login
        else:
            # Handle invalid login here
            pass
    return render(request, 'login.html')


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})



def home(request):
    return render(request, 'recipes/index.html')


def search_recipes(request):
    ingredient = request.GET.get('ingredient', '')
    recipes = Recipe.objects.filter(ingredients__icontains=ingredient)
    recipe_data = [
        {'id': recipe.id, 'name': recipe.name, 'ingredients': recipe.ingredients, 'cuisine': recipe.cuisine}
        for recipe in recipes
    ]
    return JsonResponse(recipe_data, safe=False)
from django.shortcuts import render
 
def cuisines(request):
   recipes = Recipe.objects.all()
   return render(request, 'recipes/cuisines.html')

'''
def snacks(request):
    return render(request, 'recipes/snacks.html')
'''
def snacks(request):
    recipes = Recipe.objects.filter(category='snacks')
    for recipe in recipes:
        recipe.split_ingredients = recipe.ingredients.split(',')
        recipe.split_steps = recipe.steps.split('.')
    return render(request, 'recipes/snacks.html', {'recipes': recipes})

def desserts(request):
    return render(request, 'recipes/desserts.html')

def lunch(request):
    return render(request, 'recipes/lunch.html')

def breakfast(request):
    return render(request, 'recipes/breakfast.html')

def dinner(request):
    return render(request, 'recipes/dinner.html')
'''
def snacks_view(request):
    snacks = Recipe.objects.filter(category="Snacks")
    return render(request, 'snacks.html', {'recipes': snacks})
'''