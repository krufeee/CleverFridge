from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from CleverFridge.ingredients.models import IngredientCreateModel

UserModel = get_user_model()

class RecipeCreateModel(models.Model):
    DEFAULT_IMAGE = 'media_files/NoPictureForRecipe.jpg'
    INSTRUCTIONS_MAX_LEN = 3000
    TYPE_MAX_LEN = 10
    RECIPE_NAME_MAX_LEN = 30
    SALAD = 'salad'
    APPETIZER = 'appetizer'
    MAIN_DISH = 'main dish'
    DESSERT = 'dessert'
    Types_of_meals = (
        (APPETIZER,APPETIZER),
        (MAIN_DISH, MAIN_DISH),
        (DESSERT,DESSERT),
        (SALAD,SALAD),

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
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    ingredients = models.ManyToManyField(
        IngredientCreateModel,

    )

    def get_absolute_url(self):
        return reverse("detail recipe", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.recipe_name}')
        return super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.recipe_name} - {self.recipe_type}'


    class Meta:
        verbose_name = 'Add Recipe'