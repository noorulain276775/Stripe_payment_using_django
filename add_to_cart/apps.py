from django.apps import AppConfig
from django.core.signals import request_finished


class AddToCartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'add_to_cart'

    def ready(self):
        from . import signals
        request_finished.connect(signals.my_callback)
