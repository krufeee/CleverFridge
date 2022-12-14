from django.contrib.auth import get_user_model
from django.db import models

from CleverFridge.ingredients.models import IngredientCreateModel

UserModel = get_user_model()

class RecipeCreateModel(models.Model):
    DEFAULT_IMAGE = 'media_files/NoPictureForRecipe.jpg'
    INSTRUCTIONS_MAX_LEN = 3000
    TYPE_MAX_LEN = 10
    RECIPE_NAME_MAX_LEN = 30
    APPETIZER = 'appetizer'
    MAIN_DISH = 'main dish'
    DESSERT = 'dessert'
    Types_of_meals = (
        (APPETIZER,APPETIZER),
        (MAIN_DISH, MAIN_DISH),
        (DESSERT,DESSERT),

    )

    recipe_name = models.CharField(
        max_length=RECIPE_NAME_MAX_LEN,
        null=False,
        blank=False,
    )

    recipe_type = models.CharField(
        max_length=TYPE_MAX_LEN,
        choices=Types_of_meals,
        blank=True,
        null=True,

    )


    recipe_cooking_instruction = models.TextField()

    recipe_picture = models.ImageField(
        upload_to= 'recipes',
        null=True,
        blank=True,
        default='NoPictureForRecipe.jpg',
    )


    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,

    )

    ingredients = models.ManyToManyField(
        IngredientCreateModel,

    )

    def __str__(self):
        return f'{self.recipe_name} - {self.recipe_type}'

    class Meta:
        verbose_name = 'Add Recipe'