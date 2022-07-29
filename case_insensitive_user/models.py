from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager as DefaultUserManager


class UserManager(DefaultUserManager):
    def get_by_natural_key(self, username):
        return self.get(**{f'{self.model.USERNAME_FIELD}__iexact': username})


class User(AbstractUser):
    objects = UserManager()

    @classmethod
    def normalize_username(cls, username):
        return super().normalize_username(username).casefold()
