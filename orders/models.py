from django.conf import settings
from django.db import models

from products.models import Product


User = settings.AUTH_USER_MODEL


class Order(models.Model):

    STATUS_CHOICES = (
        ("new", "New"),
        ("confirmed", "Confirmed"),
        ("processing", "Processing"),
        ("sent", "Sent"),
        ("done", "Done"),
        ("canceled", "Canceled"),
    )

    user = models.ForeignKey(
        User,
        related_name="orders",
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="new"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    delivery_address = models.CharField(
        max_length=500
    )

    def __str__(self):

        return f"Order #{self.id}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        related_name="items",
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):

        return f"{self.product} x {self.quantity}"