from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductListView(generics.ListCreateAPIView):
    """
    Список товаров
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    """
    Детали товара
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer