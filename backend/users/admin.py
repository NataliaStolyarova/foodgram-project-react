from django.contrib import admin

from .models import Follow, User


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
    list_filter = ('email', 'first_name', 'username')
    search_fields = ('email', 'username', 'first_name', 'last_name')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author'
    )
    search_fields = ('author', 'user')
    list_filter = ('author', 'user')

    def get_queryset(self, request):
        return Follow.objects.select_related(
            'user', 'author'
        )
