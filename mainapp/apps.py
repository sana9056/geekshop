from django.apps import AppConfig
from django.conf import settings
from django.conf.urls.static import static

class MainappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mainapp'
