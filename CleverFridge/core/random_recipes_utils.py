import random


from CleverFridge.core.recipe_utils import return_list_of_objects_by_list_of_pk
from CleverFridge.recipes.models import RecipeCreateModel
def get_possible_recipe_types_returns_list():
    list_of_types = []
    types = RecipeCreateModel.Types_of_meals
    for option in types:
        list_of_types.append(option[0])
    return list_of_types

def filter_recipes_by_type(list_of_pk):
    list_of_possible_recipe = return_list_of_objects_by_list_of_pk(list_of_pk)
    types = get_possible_recipe_types_returns_list()
    list_of_possible_recipes_filtered_by_type = []
    added_type = []

    for _ in types:
        for qset in list_of_possible_recipe:
            dic = (qset.values('recipe_type')[0])
            if dic['recipe_type'] not in added_type:
                list_of_possible_recipes_filtered_by_type.append(qset)
                added_type.append(dic['recipe_type'])
    return list_of_possible_recipes_filtered_by_type


def get_random_possible_recipe_by_recipe_type(list_of_qsets):
    list_of_random_possible_recipe = []
    for qset in list_of_qsets:
        if qset:
            selected = random.choice(qset)
            list_of_random_possible_recipe.append(selected)
        else:
            pass
    return list_of_random_possible_recipe