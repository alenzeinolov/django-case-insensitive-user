from django.test import TestCase

from case_insensitive_user.models import User


class UserTestCase(TestCase):
    TEST_USERNAME = 'test_username'
    TEST_EMAIL = 'test_username@example.com'

    def test_username_always_lowercase(self):
        user = User.objects.create_user(
            username=self.TEST_USERNAME.upper()
        )
        self.assertEqual(user.username, self.TEST_USERNAME)

    def test_username_lookup_case_insensitive(self):
        User.objects.create_user(username=self.TEST_USERNAME)
        self.assertIsNotNone(
            User.objects.get_by_natural_key(self.TEST_USERNAME.upper())
        )
