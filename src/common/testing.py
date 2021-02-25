from django.contrib.auth import get_user_model
from django.test import Client
from rest_framework_jwt.settings import api_settings

User = get_user_model()


def get_api_client(email=None, user=None):
    email = email or 'test_email@localhost'
    user = user or User.objects.create(username=email, email=email, password='notqwerty2')
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

    payload = jwt_payload_handler(user)
    token = jwt_encode_handler(payload)
    headers = {'HTTP_AUTHORIZATION': 'JWT {}'.format(token), 'content_type': 'application/json'}

    return Client(), headers
