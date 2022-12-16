from django.conf import settings as django_settings


class Settings:
    @property
    def _user_settings(self):
        return getattr(django_settings, "CASE_INSENSITIVE_USER", {})

    @property
    def VERBOSE_NAME(self):
        return self._user_settings.get("VERBOSE_NAME", "Case Insensitive User")

    @property
    def CASE_INSENSITIVE_EMAIL(self):
        return self._user_settings.get("CASE_INSENSITIVE_EMAIL", False)


settings = Settings()
