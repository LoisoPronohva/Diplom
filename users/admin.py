from django.contrib import admin
from .models import User, Address


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ("id", "username", "email")


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "city", "street", "postal_code")