import pytest
from django.contrib.auth import get_user_model
from faker import Faker

from entities.bet.models import Bet
from entities.game.models import Game

fake = Faker()
User = get_user_model()


@pytest.fixture
@pytest.mark.django_db
def user_factory():
    def create_user(email=None, username=None):
        email = email or fake.email()
        username = username or fake.name()
        user = User.objects.create(username=username, email=email, balance=1000)
        user.set_password('notqwerty2')
        user.save()
        return user
    return create_user


@pytest.fixture
@pytest.mark.django_db
def game_factory():
    def create_game(user=None):
        user = user or user_factory()
        game = Game.objects.create(user=user)
        return game
    return create_game


@pytest.fixture
@pytest.mark.django_db
def bet_factory():
    def create_bet(user=None, game=None):
        user = user or user_factory()
        game = game or Game.objects.create(user=user)
        bet = Bet.objects.create(game=game, amount=100, chosen_equal=Bet.RIGHT)
        return bet
    return create_bet
