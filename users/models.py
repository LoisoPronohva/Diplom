from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_supplier = models.BooleanField(default=False)