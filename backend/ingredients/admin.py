from django.contrib import admin
from .models import Ingredient

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit',
        )
    search_fields = (
        'name',
        'measurement_unit',
        )
    list_filter = (
        'name',
        'measurement_unit',
        )
    empty_value_display = '-empty-'
