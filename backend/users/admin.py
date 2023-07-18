from django.contrib import admin
from admin_auto_filters.filters import AutocompleteFilter

from .models import Follow, User


class UserFilter(AutocompleteFilter):
    title = 'User'
    field_name = 'email'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'email',
        'username',
        'first_name',
        'last_name'
    )
    list_editable = (
        'username',
        'first_name',
        'last_name'
    )
    search_fields = ('email', 'username')
    list_filter = (UserFilter,)


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author'
    )

    def get_queryset(self, request):
        return Follow.objects.select_related(
            'user', 'author'
        )
