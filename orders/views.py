from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer


class OrderListView(generics.ListCreateAPIView):
    """
    Список заказов
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    """
    Детали заказа
    """

    queryset = Order.objects.all()
    serializer_class = OrderSerializer