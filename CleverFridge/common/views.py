from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views import generic

from CleverFridge.common.models import HomepageWellcomeTextModel
from CleverFridge.core.random_recipes_utils import get_random_possible_recipe_by_recipe_type, filter_recipes_by_type, \
    get_params
from CleverFridge.core.recipe_utils import get_possible_recipes_return_list_of_pk
from CleverFridge.recipes.models import RecipeCreateModel


class IndexView(generic.TemplateView):
    template_name = 'common/index.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        result['description'] = HomepageWellcomeTextModel.objects.first()   #fixed after deadline , was .get()
        return result

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        return super(IndexView, self).dispatch(request, *args, **kwargs)


class HomepageView(LoginRequiredMixin, generic.TemplateView):
    SALAD = RecipeCreateModel.SALAD
    APPETIZER = RecipeCreateModel.APPETIZER
    MAIN_DISH = RecipeCreateModel.MAIN_DISH
    DESSERT = RecipeCreateModel.DESSERT

    template_name = 'common/homepage.html'

    def get_context_data(self, **kwargs):
        result = super().get_context_data(**kwargs)
        current_user = self.request.user.username
        all_possible_recipes =get_possible_recipes_return_list_of_pk(self.request.user.pk)
        filtered_recipes = filter_recipes_by_type(all_possible_recipes)
        random_recipes_beta= get_random_possible_recipe_by_recipe_type(filtered_recipes)
        random_recipes = get_params(random_recipes_beta)
        result['random_recipes'] = random_recipes
        # result['recipe_set'] = random_recipes[4]
        result['current_user'] = current_user
        return result
