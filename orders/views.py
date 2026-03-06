from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from django.db.models import Prefetch

from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderListView(generics.ListAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):

        return (
            Order.objects
            .filter(user=self.request.user)
            .prefetch_related(
                Prefetch("items", queryset=OrderItem.objects.select_related("product"))
            )
        )


class OrderDetailView(generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):

        return (
            Order.objects
            .filter(user=self.request.user)
            .prefetch_related("items__product")
        )


class OrderCreateView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)