import random


from CleverFridge.core.recipe_utils import return_list_of_objects_by_list_of_pk, return_possible_recipe_params
from CleverFridge.recipes.models import RecipeCreateModel
def get_possible_recipe_types_returns_list():
    list_of_types = []
    types = RecipeCreateModel.Types_of_meals
    for option in types:
        list_of_types.append(option[0])
    return list_of_types

def filter_recipes_by_type(list_of_pk):
    list_of_possible_recipe = return_list_of_objects_by_list_of_pk(list_of_pk)
    dict_of_possible_recipes_filtered_by_type = {}
    for qset in list_of_possible_recipe:
        dic = qset.values('recipe_type')[0]['recipe_type']
        if dic not in dict_of_possible_recipes_filtered_by_type.keys():
            dict_of_possible_recipes_filtered_by_type[dic] = []
            dict_of_possible_recipes_filtered_by_type[dic].append(qset)
        else:
            dict_of_possible_recipes_filtered_by_type[dic].append(qset)

    return dict_of_possible_recipes_filtered_by_type


def get_random_possible_recipe_by_recipe_type(dict_of_qsets):
    list_of_random_possible_recipe = []
    for recipe_type , qset in dict_of_qsets.items():
        if qset:
            selected = random.choice(qset)
            list_of_random_possible_recipe.append(selected)
        else:
            pass
    return list_of_random_possible_recipe

def get_params(list_of_qsets):
    qsets_params_list = []
    for qset in list_of_qsets:
        current_list = []
        current_name = qset.values('recipe_name')[0]['recipe_name']
        current_type = qset.values('recipe_type')[0]['recipe_type']
        current_image = qset.values('recipe_picture')[0]['recipe_picture']
        current_slug = qset.values('slug')[0]['slug']
        recipe = qset
        current_list.append(current_name)
        current_list.append(current_type)
        current_list.append(current_image)
        current_list.append(current_slug)
        current_list.append(recipe)
        qsets_params_list.append(current_list)
    return qsets_params_list
