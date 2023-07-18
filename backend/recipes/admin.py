from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag


class AuthorFilter(AutocompleteFilter):
    title = 'Автор'
    field_name = 'author'


class TagFilter(AutocompleteFilter):
    title = 'Тег'
    field_name = 'tags'


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'name',
        'text',
        'cooking_time',
        'get_tags',
        'get_favorite_count'
    )
    list_filter = (AuthorFilter, TagFilter)

    def get_queryset(self, response):
        return Recipe.objects.select_related(
            'author'
        ).prefetch_related(
            'tags', 'ingredients')

    @admin.display(description='Тэги')
    def get_tags(self, obj):
        list_ = [tag.name for tag in obj.tags.all()]
        return ', '.join(list_)

    @admin.display(description='В избранном')
    def get_favorite_count(self, obj):
        return Favorite.objects.filter(recipe=obj).count()


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'color',
        'slug'
    )
    search_fields = ('name',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'measurement_unit'
    )


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe'
    )

    def get_queryset(self, response):
        return Favorite.objects.select_related(
            'user', 'recipe'
        )


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe'
    )

    def get_queryset(self, response):
        return ShoppingCart.objects.select_related(
            'user', 'recipe'
        )
