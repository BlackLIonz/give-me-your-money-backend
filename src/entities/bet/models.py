import random

from django.db import models

from common.models import Model

CARD_RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
CARD_SUIT = ['c', 'd', 'h', 's']


def card_generator():
    rank = random.choice(CARD_RANK)
    suit = random.choice(CARD_SUIT)
    card = rank + suit
    return card


class Bet(Model):
    SAME = 'S'
    LEFT = 'L'
    RIGHT = 'R'
    EQUAL_CHOICES = (
        (SAME, "Same"),
        (LEFT, "Left"),
        (RIGHT, "Right"),
    )
    game = models.ForeignKey('game.Game', on_delete=models.CASCADE, related_name='bets')
    amount = models.PositiveIntegerField()
    chosen_equal = models.CharField(max_length=1, choices=EQUAL_CHOICES)
    left_card = models.CharField(max_length=3, blank=True)
    right_card = models.CharField(max_length=3, blank=True)

    @property
    def is_winner(self):
        try:
            left_value = CARD_RANK.index(self.left_card[:-1])
            right_value = CARD_RANK.index(self.right_card[:-1])
            if self.chosen_equal == self.SAME:
                return left_value == right_value
            elif self.chosen_equal == self.LEFT:
                return left_value > right_value
            elif self.chosen_equal == self.RIGHT:
                return right_value > left_value
            else:
                return False
        except Exception:
            return False
