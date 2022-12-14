from CleverFridge.ingredients.models import IngredientAddToFridgeModel


def get_ingredients_by_pk(user_pk):
    ingredients = IngredientAddToFridgeModel.objects.filter(user_id=user_pk)
    return ingredients

def return_list_ingredients(user_pk):
    ingredients_list = []
    products = IngredientAddToFridgeModel.objects.filter(user_id=user_pk)
    for product in products:
        ingredients_list.append(product.ingredients.name)

    return ingredients_list