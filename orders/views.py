from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


class OrderListView(generics.ListCreateAPIView):
    """
    Список заказов и создание заказа
    """

    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("items")
    )

    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    """
    Детали заказа
    """

    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("items")
    )

    serializer_class = OrderSerializer