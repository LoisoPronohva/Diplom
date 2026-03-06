from rest_framework.views import APIView
from rest_framework.response import Response

# Заглушка для будущих эндпоинтов
class CartView(APIView):
    def get(self, request):
        return Response({"message": "Cart endpoint is empty"})