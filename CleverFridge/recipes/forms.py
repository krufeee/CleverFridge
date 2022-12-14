import uuid

from django import forms

from CleverFridge.ingredients.models import IngredientCreateModel
from CleverFridge.recipes.models import RecipeCreateModel


class RecipeCreateForm(forms.ModelForm):


    ingredients = forms.ModelMultipleChoiceField(
        queryset=IngredientCreateModel.objects.all().filter().order_by('name'),
        # widget=forms.SelectMultiple,
        widget=forms.CheckboxSelectMultiple,
        # empty_label=None,
        # to_field_name='name'
    )

    # def clean_recipe_picture(self):
    #     if self.cleaned_data['recipe_picture'] != "NoPictureForRecipe.jpg":
    #         recipe_picture = self.cleaned_data['recipe_picture']
    #         recipe_picture.name = str(uuid.uuid4())
    #         return recipe_picture

    class Meta:
        model = RecipeCreateModel
        exclude = ('user',)