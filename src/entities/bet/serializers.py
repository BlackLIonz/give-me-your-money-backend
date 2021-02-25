from rest_framework import serializers

from entities.bet.models import Bet
from entities.game.models import Game


class BetSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    game_id = serializers.UUIDField(format='hex')
    left_card = serializers.CharField(read_only=True)
    right_card = serializers.CharField(read_only=True)
    is_winner = serializers.BooleanField(read_only=True)

    class Meta:
        model = Bet
        fields = (
            'id',
            'game_id',
            'amount',
            'chosen_equal',
            'left_card',
            'right_card',
            'is_winner',
        )
        ordering = ('-created_at',)
