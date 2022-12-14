from django.contrib import admin

from CleverFridge.recipes.models import RecipeCreateModel


@admin.register(RecipeCreateModel)
class RecipeCreateAdmin(admin.ModelAdmin):
    pass