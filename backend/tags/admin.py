from django.contrib import admin
from .models import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug',
        )
    search_fields = (
        'name',
        'color',
        'slug',
        )
    list_filter = (
        'name',
        'color',
        'slug',
        )
    prepopulated_fields = {'slug': ('name',)}
    empty_value_display = '-empty-'