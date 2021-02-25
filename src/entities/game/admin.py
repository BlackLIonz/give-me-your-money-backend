from django.contrib import admin

from entities.game.models import Game


class GameAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user_email',
        'user_id',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'id',
        'user_id',
    )


admin.site.register(Game, GameAdmin)
