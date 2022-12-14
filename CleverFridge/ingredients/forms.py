from django import forms

from CleverFridge.ingredients.models import IngredientAddToFridgeModel, IngredientCreateModel


class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = IngredientAddToFridgeModel
        fields = '__all__'


class IngredientAddToFridgeForm(forms.ModelForm):
    ingredients = forms.ModelChoiceField(
        queryset=IngredientCreateModel.objects.all(),
        empty_label=None,
        # to_field_name='name'
    )
    class Meta:
        model = IngredientAddToFridgeModel
        exclude = ('user',)




