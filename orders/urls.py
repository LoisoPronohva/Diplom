from django.urls import path

from .views import (
    OrderListView,
    OrderDetailView,
    OrderCreateView
)

urlpatterns = [

    path(
        "",
        OrderListView.as_view(),
        name="orders-list"
    ),

    path(
        "<int:pk>/",
        OrderDetailView.as_view(),
        name="orders-detail"
    ),

    path(
        "create/",
        OrderCreateView.as_view(),
        name="orders-create"
    ),
]