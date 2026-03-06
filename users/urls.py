from django.urls import path

from .views import (
    RegisterView,
    AddressListCreateView,
    AddressDeleteView
)

urlpatterns = [

    path(
        "register/",
        RegisterView.as_view(),
        name="register"
    ),

    path(
        "addresses/",
        AddressListCreateView.as_view(),
        name="addresses"
    ),

    path(
        "addresses/<int:pk>/",
        AddressDeleteView.as_view(),
        name="address-delete"
    ),
]