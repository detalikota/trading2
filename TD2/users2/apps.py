from django.apps import AppConfig


class Users2Config(AppConfig):
    name = 'users2'

    def ready(self):
        import users2.signals
