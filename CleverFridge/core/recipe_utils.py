from CleverFridge.core.ingredients_utils import return_list_ingredients
from CleverFridge.recipes.models import RecipeCreateModel


def get_recipes_by_pk(user_pk):
    recipe = RecipeCreateModel.objects.filter(user_id=user_pk)
    return recipe

def get_recipe_by_recipe_pk(pk):
    recipe = RecipeCreateModel.objects.filter(pk=pk)
    return recipe

def get_all_recipes_ingredients_returns_dict():
    all_recipes = RecipeCreateModel.objects.all()
    ingredients_dict = {}
    for recipe in all_recipes:
        ingredients_dict[recipe.pk] = []
        for ingredient in recipe.ingredients.all():
            ingredients_dict[recipe.pk].append(ingredient.name)
    return ingredients_dict

def get_possible_recipes_return_list_of_pk(user_pk):
    all_recipe_dict = get_all_recipes_ingredients_returns_dict()
    user_ingredients_list = return_list_ingredients(user_pk)
    possible_recipes_list_of_pk = []
    for key,value in all_recipe_dict.items():
        if all(x in user_ingredients_list for x in value):
            possible_recipes_list_of_pk.append(key)
    return possible_recipes_list_of_pk



def return_list_of_objects_by_list_of_pk(list_of_pk):
    list_of_objects = []
    for pk in list_of_pk:
        current_recipe = get_recipe_by_recipe_pk(pk)
        list_of_objects.append(current_recipe)
    return list_of_objects


def return_possible_recipe_params(qset):
    list_of_params = []
    for recipe in qset:
        for field in recipe:
            list_of_params.append(field)
    return list_of_params
