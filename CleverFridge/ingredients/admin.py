from django.contrib import admin

from CleverFridge.ingredients.forms import IngredientCreateForm
from CleverFridge.ingredients.models import IngredientCreateModel


@admin.register(IngredientCreateModel)
class Ingredients(admin.ModelAdmin):
    list_display = ('name', 'unit')
    ordering = ('name',)
