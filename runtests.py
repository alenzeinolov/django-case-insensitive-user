import sys
from pathlib import Path

import django
from django.conf import settings
from django.test.runner import DiscoverRunner

BASE_DIR = Path(__file__).resolve().parent


def setup_django():
    settings.configure(
        DEBUG=True,
        DATABASES={
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        },
        INSTALLED_APPS=(
            "django.contrib.auth",
            "django.contrib.contenttypes",
            "case_insensitive_user",
        ),
        AUTH_USER_MODEL='case_insensitive_user.User',
    )
    django.setup()


def main():
    setup_django()

    runner = DiscoverRunner(verbosity=1)
    failures = runner.run_tests(['tests'])
    if failures:
        sys.exit(failures)
    sys.exit(0)


if __name__ == '__main__':
    main()
