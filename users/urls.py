from django.urls import path
from .views import RegisterView, AddressListCreateView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="user-register"),
    path("addresses/", AddressListCreateView.as_view(), name="address-list"),
]