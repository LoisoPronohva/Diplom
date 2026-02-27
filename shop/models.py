from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

class Product(models.Model):
    name = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    attributes = models.JSONField(default=dict, blank=True)
    is_available = models.BooleanField(default=True)