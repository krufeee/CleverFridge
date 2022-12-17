from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from CleverFridge.core.ingredients_utils import get_ingredients_by_pk
from CleverFridge.ingredients.forms import IngredientAddToFridgeForm
from CleverFridge.ingredients.models import IngredientAddToFridgeModel


class MyIngredientsView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'ingredients/my-ingredients.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)

        ingredients = get_ingredients_by_pk(self.request.user.pk)
        result['products'] = ingredients
        return result


class IngredientAddToFridgeView(LoginRequiredMixin, generic.CreateView):
    template_name = './ingredients/add-ingredient.html'
    form_class = IngredientAddToFridgeForm
    success_url = reverse_lazy('my ingredients')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)



class IngredientEditInFridgeView(LoginRequiredMixin, generic.UpdateView):
    template_name = './ingredients/edit-ingredient.html'
    model = IngredientAddToFridgeModel
    success_url = reverse_lazy('my ingredients')
    fields = ('ingredient', 'amount', 'unit')


class IngredientDeleteFromFridgeView(LoginRequiredMixin, generic.DeleteView):
    template_name = './ingredients/delete-ingredient.html'
    model = IngredientAddToFridgeModel
    success_url = reverse_lazy('my ingredients')
