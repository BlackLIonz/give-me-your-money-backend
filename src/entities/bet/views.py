from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from entities.bet.models import Bet
from entities.bet.serializers import BetSerializer


class BetViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    serializer_class = BetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Bet.objects.all()

    def get_queryset(self):
        return self.queryset.filter(game__user_id=self.request.user.id)
