from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            password="test123"
        )
        self.assertEqual(user.email, "test@example.com")