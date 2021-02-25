import pytest

from common.testing import get_api_client


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
def test_create_game(client, user_factory):
    user = user_factory()
    token = login(user, client)

    response = client.post(
        f'/api/v1/games/',
        data={},
        **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
    )
    assert response.status_code == 201
    assert response.data['user_id'] == user.id.hex


@pytest.mark.django_db
def test_create_game_by_other_user(client, game_factory, user_factory):
    user_1 = user_factory()
    user_2 = user_factory()

    token_1 = login(user_1, client)
    game_factory(user_2)
    response = client.get(
        f'/api/v1/games/',
        data={},
        **{'HTTP_AUTHORIZATION': f'Bearer {token_1}'}
    )
    assert response.status_code == 200
    assert len(response.data.get('results')) == 0


@pytest.mark.django_db
def test_not_allowed_methods(client, game_factory, user_factory):
    user = user_factory()
    token = login(user, client)
    game = game_factory(user)
    response = client.delete(
        f'/api/v1/games/{game.id.hex}/',
        **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
    )
    assert response.status_code == 405
    response = client.patch(
        f'/api/v1/games/{game.id.hex}/',
        data={'user_id': game.user.id.hex},
        **{'HTTP_AUTHORIZATION': f'Bearer {token}'}
    )
    assert response.status_code == 405
