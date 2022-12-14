from django.urls import path

from CleverFridge.ingredients.views import IngredientAddToFridgeView, IngredientEditInFridgeView, IngredientDeleteFromFridgeView, \
    MyIngredientsView

urlpatterns = (
    path('', MyIngredientsView.as_view(), name='my ingredients'),
    path('add/', IngredientAddToFridgeView.as_view(), name='add ingredient'),
    path('edit/<int:pk>/', IngredientEditInFridgeView.as_view(), name='edit ingredient'),
    path('delete/<int:pk>/', IngredientDeleteFromFridgeView.as_view(), name='delete ingredient'),
)