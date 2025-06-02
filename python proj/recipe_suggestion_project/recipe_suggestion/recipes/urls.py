from django.urls import path
from . import views

urlpatterns = [
    #path('register/', views.register, name='register'),
    #path('login/', views.login_view, name='login'),
    #  path('recipe/<int:id>/', views.recipe_detail, name='recipe_detail'),
    path('', views.home, name='home'),
    path('search-recipes/', views.search_recipes, name='search_recipes'),
    path('cuisines/', views.cuisines, name='cuisines'),
    path('snacks/', views.snacks, name='snacks'),
    path('desserts/', views.desserts, name='desserts'),
    path('lunch/', views.lunch, name='lunch'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('dinner/', views.dinner, name='dinner'),
    

   

]
