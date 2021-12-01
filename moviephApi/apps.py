from django.apps import AppConfig


class MoviephapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'moviephApi'

    def ready(self):
        from .moviecrawler import startScheduler
        print("Scheduler Launched!")
        startScheduler()

