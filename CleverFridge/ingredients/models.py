from django.contrib.auth import get_user_model
from django.db import models

UserModel = get_user_model()


class IngredientCreateModel(models.Model):
    INGREDIENT_MAX_LEN = 15
    UNIT_MAX_LEN = 10
    GRAMS = 'gr.'
    PIECES = 'pieces'
    MILLILITERS = 'ml.'
    Units = (
        (GRAMS,GRAMS),
        (MILLILITERS, MILLILITERS),
        (PIECES,PIECES),

    )

    name = models.CharField(
        max_length=INGREDIENT_MAX_LEN,
        null=False,
        blank=False,
        unique=True,
    )


    unit = models.CharField(
        choices=Units,
        max_length=UNIT_MAX_LEN,
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.name} - {self.unit}'

    class Meta:
        verbose_name = 'Add Ingredient'


class IngredientAddToFridgeModel(models.Model):

    ingredients = models.OneToOneField(

        IngredientCreateModel,
        on_delete=models.CASCADE,
        error_messages={'unique_check':'You already have this ingredient in your fridge.'},

    )


    #todo when cook app is implemented

    # amount = models.PositiveIntegerField(
    #     blank=False,
    #     null=False,
    # )


    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        blank=True,
        null=True,

    )

