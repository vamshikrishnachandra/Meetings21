from django.apps import AppConfig


class Meetings21AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Meetings21app'

    def ready(self):
        import Meetings21app.signals  # Import the signals here
