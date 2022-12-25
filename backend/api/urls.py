from django.urls import include, path
from rest_framework import routers
from .views import (
    RecipeViewSet,
    IngredientViewSet,
    TagViewSet,
    AddDeleteFavoriteRecipe,
    AddDeleteShoppingCart,
    AddAndDeleteSubscribe,
)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet, basename='recipes')
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'tags', TagViewSet, basename='tags')

urlpatterns = [
    path(
        'users/<int:user_id>/subscribe/',
        AddAndDeleteSubscribe.as_view(),
        name='subscribe'),
    path(
        'users/subscriptions/',
        AddAndDeleteSubscribe.as_view(),
        name='subscribe'),
    path(
        'recipes/<int:recipe_id>/favorite/',
        AddDeleteFavoriteRecipe.as_view(),
        name='favorite_recipe'),
    path(
        'recipes/<int:recipe_id>/shopping_cart/',
        AddDeleteShoppingCart.as_view(),
        name='shopping_cart'),
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]
