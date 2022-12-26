from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic

from CleverFridge.core.recipe_utils import get_recipes_by_pk, \
    get_possible_recipes_return_list_of_pk, return_list_of_objects_by_list_of_pk, return_possible_recipe_params, \
    get_recipes_by_slug
from CleverFridge.recipes.forms import RecipeCreateForm
from CleverFridge.recipes.models import RecipeCreateModel


class MyRecipesShowView(LoginRequiredMixin, generic.ListView):
    template_name = 'recipes/my-recipes.html'
    model = RecipeCreateModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        recipes = get_recipes_by_pk(self.request.user.pk)
        context['recipes'] = recipes
        return context


class RecipeCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'recipes/add-recipe.html'
    form_class = RecipeCreateForm
    success_url = reverse_lazy('my recipes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class RecipeDetailsView(generic.DetailView):
    template_name = 'recipes/detail-recipe.html'
    model = RecipeCreateModel

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['requested_user'] = self.request.user.pk
        return result


class RecipeEditView(LoginRequiredMixin, generic.UpdateView):
   template_name = 'recipes/edit-recipe.html'
   model = RecipeCreateModel
   form_class = RecipeCreateForm
   success_url = reverse_lazy('my recipes')
   #
   # def get_context_data(self, **kwargs):
   #     result = super().get_context_data(**kwargs)
   # fields = (
   #     'recipe_name',
   #     'recipe_type',
   #     'recipe_cooking_instruction',
   #     'recipe_picture',
   #     ''
   # )


class RecipeDeleteView(LoginRequiredMixin, generic.DeleteView):
   template_name = 'recipes/delete-recipe.html'
   model = RecipeCreateModel
   success_url = reverse_lazy('my recipes')



class PossibleRecipesView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'recipes/possible-recipes.html'
    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        possible_recipes = get_possible_recipes_return_list_of_pk(self.request.user.pk)
        object_list = return_list_of_objects_by_list_of_pk(possible_recipes)
        fields = return_possible_recipe_params(object_list)
        result['possible_recipes']= fields

        return result
