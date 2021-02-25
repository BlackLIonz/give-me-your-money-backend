import pytest

from entities.bet.models import Bet
from entities.users.models import User


def login(user, client):
    response = client.post(
        '/api/v1/login/',
        data={
            'email': user.email,
            'username': user.username,
            'password': 'notqwerty2',
        }
    )
    return response.data['access']


@pytest.mark.django_db
def test_make_bet(client, user_factory, game_factory):
    user = user_factory()
    game = game_factory(user)
    token = login(user, client)

    response = client.post(
        f'/api/v1/bets/',
        data={
            'game_id': game.id.hex,
            'amount': 100,
            'chosen_equal': Bet.RIGHT
        },
        **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
    )
    assert response.status_code == 201
    assert response.data['game_id'] == game.id.hex
    assert response.data['left_card']
    assert response.data['right_card']
    assert (
        User.objects.get(id=user.id).balance
        == user.balance + 100 if response.data['is_winner'] else user.balance - 100
    )


@pytest.mark.django_db
def test_create_game_by_other_user(client, bet_factory, user_factory):
    user_1 = user_factory()
    user_2 = user_factory()

    token_1 = login(user_1, client)
    bet_factory(user_2)
    response = client.get(
        f'/api/v1/bets/',
        data={},
        **{'HTTP_AUTHORIZATION': f'Bearer {token_1}'}
    )
    assert response.status_code == 200
    assert len(response.data.get('results')) == 0


@pytest.mark.django_db
def test_not_allowed_methods(client, bet_factory, user_factory):
    user = user_factory()
    token = login(user, client)
    bet = bet_factory(user)
    response = client.patch(
        f'/api/v1/bets/{bet.id.hex}/',
        data={'game_id': bet.game.id.hex},
        **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
    )
    assert response.status_code == 405
    response = client.delete(
        f'/api/v1/bets/{bet.id.hex}/',
        **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
    )
    assert response.status_code == 405
