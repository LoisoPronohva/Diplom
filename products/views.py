from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from django_filters.rest_framework import DjangoFilterBackend

from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilter
from .services import import_products_from_csv, export_products_to_csv


class ProductListView(generics.ListAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [AllowAny]

    filter_backends = [DjangoFilterBackend]

    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):

    queryset = Product.objects.all()

    serializer_class = ProductSerializer

    permission_classes = [AllowAny]


class ProductImportView(APIView):

    def post(self, request):

        file = request.FILES.get("file")

        import_products_from_csv(file)

        return Response({"status": "import completed"})


class ProductExportView(APIView):

    def get(self, request):

        data = export_products_to_csv()

        return Response(data)