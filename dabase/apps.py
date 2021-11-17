from django.apps import AppConfig


class DabaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dabase'

    def ready(self):
        import dabase.signals