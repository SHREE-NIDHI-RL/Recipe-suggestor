'''
from django.db import models

from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    steps = models.TextField()
    cuisine = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recipes/', null=True, blank=True)

    def __str__(self):
        return self.name
'''
from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=100)
    ingredients = models.TextField()
    steps = models.TextField()
    category = models.CharField(max_length=50,default='Snacks')  # e.g., Snacks, Desserts, etc.

    def __str__(self):
        return self.name
