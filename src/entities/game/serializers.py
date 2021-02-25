from rest_framework import serializers

from entities.game.models import Game


class GameSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True, format='hex')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_id = serializers.UUIDField(read_only=True, format='hex')

    class Meta:
        model = Game
        fields = (
            'id',
            'user',
            'user_id',
        )
        ordering = ('-created_at',)
