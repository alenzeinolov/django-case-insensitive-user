from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DefaultUserManager

from case_insensitive_user.conf import settings


class UserManager(DefaultUserManager):
    @classmethod
    def normalize_email(cls, email):
        email = super().normalize_email(email)
        if settings.CASE_INSENSITIVE_EMAIL:
            return email.casefold()
        return email

    def get_by_natural_key(self, username):
        return self.get(**{f"{self.model.USERNAME_FIELD}__iexact": username})


class User(AbstractUser):
    objects = UserManager()

    @classmethod
    def normalize_username(cls, username):
        return super().normalize_username(username).casefold()
