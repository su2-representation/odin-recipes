from django.views.generic import ListView, DetailView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    template_name = 'index.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'
