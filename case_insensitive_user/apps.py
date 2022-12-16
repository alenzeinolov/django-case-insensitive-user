from django.apps import AppConfig

from case_insensitive_user.conf import settings


class CaseInsensitiveUserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "case_insensitive_user"
    verbose_name = settings.VERBOSE_NAME
