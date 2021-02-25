from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from entities.bet.models import Bet, card_generator


@receiver(post_save, sender=Bet)
def bet_post_save_signal(sender, instance: Bet, created: bool, signal, **kwargs):
    if created:
        instance.left_card = card_generator()
        instance.right_card = card_generator()
        while instance.right_card == instance.left_card:
            instance.right_card = card_generator()
        instance.save()
        user = instance.game.user
        if instance.is_winner:
            user.balance += instance.amount
        else:
            user.balance -= instance.amount
        user.save(update_fields=['balance'])

