from django.contrib import admin

from entities.bet.models import Bet


class BetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'game_id',
        'amount',
        'chosen_equal',
        'is_winner',
        'left_card',
        'right_card',
        'created_at',
        'updated_at',
    )

    search_fields = (
        'id',
        'game_id',
        'game_id__user_id',
    )


admin.site.register(Bet, BetAdmin)
