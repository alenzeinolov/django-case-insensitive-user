from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from case_insensitive_user.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    pass
