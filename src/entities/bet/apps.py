from django.apps import AppConfig


class BetConfig(AppConfig):
    name = 'entities.bet'

    def ready(self):
        try:
            __import__('entities.bet.signals')
        except ModuleNotFoundError:
            pass
