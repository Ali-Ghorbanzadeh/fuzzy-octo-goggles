from django.apps import AppConfig


class LogerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.loger'

    def ready(self):
        import apps.loger.signals
