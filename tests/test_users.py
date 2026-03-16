from rest_framework.test import APITestCase
from users.models import User


class UserTests(APITestCase):

    def test_create_user(self):

        data = {
            "username": "testuser",
            "password": "12345678"
        }

        response = self.client.post("/api/users/", data)

        self.assertEqual(response.status_code, 201)

    def test_get_users(self):

        User.objects.create(username="user1")

        response = self.client.get("/api/users/")

        self.assertEqual(response.status_code, 200)