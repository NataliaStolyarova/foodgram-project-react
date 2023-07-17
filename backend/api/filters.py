# from django.db.models import BooleanField, ExpressionWrapper, Q
from django_filters import rest_framework

from recipes.models import Ingredient, Recipe, Tag

CHOICES_LIST = (
    ('0', 'False'),
    ('1', 'True')
)


class CustomFilterForRecipes(rest_framework.FilterSet):
    """Кастомная фильтрация для рецептов."""

    is_favorited = rest_framework.ChoiceFilter(
        method='is_favorited_method',
        choices=CHOICES_LIST
    )
    is_in_shopping_cart = rest_framework.ChoiceFilter(
        method='is_in_shopping_cart_method',
        choices=CHOICES_LIST
    )
    author = rest_framework.NumberFilter(
        field_name='author',
        lookup_expr='exact'
    )
    tags = rest_framework.ModelMultipleChoiceFilter(
        field_name='tags__slug',
        to_field_name='slug',
        queryset=Tag.objects.all()
    )

    def is_favorited_method(self, queryset, name, value):
        if self.request.user.is_anonymous:
            return Recipe.objects.none()
        if value == '1':
            user = self.request.user
            return queryset.filter(favorites__user_id=user.id)
        return queryset

    def is_in_shopping_cart_method(self, queryset, name, value):
        if self.request.user.is_anonymous:
            return Recipe.objects.none()
        if value == '1':
            user = self.request.user
            return queryset.filter(recipe_shopping_cart__user_id=user.id)
        return queryset

    class Meta:
        model = Recipe
        fields = ('author', 'tags')


class CustomFilterForIngredients(rest_framework.FilterSet):
    """Кастомная фильтрация для ингредиентов."""

    name = rest_framework.CharFilter(field_name='name',
                                     lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ('name',)
    # name = rest_framework.CharFilter(method='filter_name')

    # class Meta:
    #     model = Ingredient
    #     fields = ('name',)

    # def filter_name(self, queryset, name, value):
    #     return queryset.filter(
    #         Q(name__istartswith=value) | Q(name__icontains=value)
    #     ).annotate(
    #         startswith=ExpressionWrapper(
    #             Q(name__istartswith=value),
    #             output_field=BooleanField()
    #         )
    #     ).order_by('-startswith')
