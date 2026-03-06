from rest_framework import generics
from .models import Product, ProductSpecification
from .serializers import ProductSerializer, ProductSpecificationSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductSpecificationListCreateView(generics.ListCreateAPIView):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer