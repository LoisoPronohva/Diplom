from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from .models import Order


User = get_user_model()


class OrderTests(APITestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            email="test@test.com",
            password="123456"
        )

        self.client.force_authenticate(self.user)

    def test_create_order(self):

        url = reverse("orders-create")

        data = {
            "delivery_address": "Test street",
            "items": []
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, 201)