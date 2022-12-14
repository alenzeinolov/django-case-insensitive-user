# django-case-insensitive-user
Small app that extends default Django user to have case-insensitive username.

## Requirements
- Python 3.7 or later
- Django 3.2 or later

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

## Features
- Works out of the box in Django admin panel
- 100% test coverage

## Configuration
Configuration is done using `CASE_INSENSITIVE_USER` optional dictionary in your settings file:
```python
CASE_INSENSITIVE_USER = {
    "VERBOSE_NAME": "Accounts",  # Display name to display in admin page for this app
    "CASE_INSENSITIVE_EMAIL": True,  # Whether to make emails case insensitive too, False by default
}
```
