from django.contrib import admin
from .models import Recipe, FavoriteRecipe, ShoppingCart, RecipeIngredient


class RecipeIngredientAdmin(admin.StackedInline):
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'text',        
        'get_ingredients',
        'cooking_time',        
        'get_tags',
        'image',
        'pub_date',
        'date_update',
        )
    inlines = (RecipeIngredientAdmin,)
    search_fields = (
        'author',
        'name',
        'text',        
        'ingredients',
        'cooking_time',        
        'tags',
        'pub_date',
        'date_update',
        )
    list_filter = (
        'author',
        'name',
        'text',        
        'ingredients',
        'cooking_time',        
        'tags',
        'pub_date',
        'date_update',
        )
    empty_value_display = '-empty-'


@admin.register(FavoriteRecipe)
class FavoriteRecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
        'favorite_date',        
        )
    search_fields = (
        'user',
        'recipe',
        'favorite_date',  
        )
    list_filter = (
        'user',
        'recipe',
        'favorite_date',  
        )
    empty_value_display = '-empty-'



@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'get_recipe',       
        )
    search_fields = (
        'user',
        'recipes',
        )
    list_filter = (
        'user',
        'recipes', 
        )
    empty_value_display = '-empty-'
