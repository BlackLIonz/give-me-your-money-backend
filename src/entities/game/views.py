from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from entities.game.models import Game
from entities.game.serializers import GameSerializer


class GameViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = GameSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Game.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user.id)
