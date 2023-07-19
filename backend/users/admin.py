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
    list_display_links = (
        'email',
        'username'
    )
    search_fields = ('email', 'username')


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'user',
        'author'
    )
    list_display_links = (
        'author',
        'user'
    )

    def get_queryset(self, request):
        return Follow.objects.select_related(
            'user', 'author'
        )
