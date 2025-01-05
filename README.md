# django-case-insensitive-user
Small app that extends default Django user to have case-insensitive username.

## Requirements
- Python 3.8 or later
- Django 4.2 or later

## Installation
1. Install `django-case-insensitive-user` using pip.
```bash
pip install requirements.txt
```
2. Add `case_insensitive_user` to `INSTALLED_APPS` list in settings.
```python
INSTALLED_APPS = [
    ...
    "case_insensitive_user",
]
```
3. Set `AUTH_USER_MODEL` to `case_insensitive_user.User` in settings.
```python
AUTH_USER_MODEL = "case_insensitive_user.User"
```

## Overriding default user model
If you want to add additional fields to the user model, you can do so by creating a new model that inherits from `case_insensitive_user.User` and adding additional fields to it. Then, set `AUTH_USER_MODEL` to the new model in settings.

```python
from django.db import models

from case_insensitive_user.models import User

class CustomUser(User):
    custom_field = models.CharField(max_length=100)
```

Make sure to set `AUTH_USER_MODEL` to the new model in settings.
```python
AUTH_USER_MODEL = "your_app.CustomUser"
```

## Features
- Works out of the box in Django admin panel
- 100% test coverage

## Configuration
Configuration is done using `CASE_INSENSITIVE_USER` optional dictionary in your settings file:
```python
CASE_INSENSITIVE_USER = {
    "VERBOSE_NAME": "Accounts",  # Display name to display in admin page for this app
    "CASE_INSENSITIVE_EMAIL": True,  # Whether to make emails case-insensitive too, False by default
}
```
