from django.urls import path

from CleverFridge.recipes.views import RecipeCreateView, MyRecipesShowView, RecipeEditView, RecipeDeleteView, \
    RecipeDetailsView, PossibleRecipesView

urlpatterns = (
    path('', MyRecipesShowView.as_view(), name='my recipes'),
    path('add/', RecipeCreateView.as_view(), name='add recipe'),
    path('details/<slug:slug>', RecipeDetailsView.as_view(), name='detail recipe'),
    path('edit/<int:pk>/', RecipeEditView.as_view(), name='edit recipe'),
    path('delete/<int:pk>/', RecipeDeleteView.as_view(), name='delete recipe'),
    path('possible-recipes/', PossibleRecipesView.as_view(), name='possible recipes'),
)