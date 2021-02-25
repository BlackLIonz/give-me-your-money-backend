from django.contrib import admin

from entities.users.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'username',
        'email',
        'balance',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'id',
        'email',
    )


admin.site.register(User, UserAdmin)
