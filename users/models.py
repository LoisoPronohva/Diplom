from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="addresses"
    )

    city = models.CharField(max_length=255)

    street = models.CharField(max_length=255)

    house = models.CharField(max_length=50)

    apartment = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} {self.street} {self.house}"