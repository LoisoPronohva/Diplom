from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    """
    Список пользователей и создание пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Детали пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class ErrorTestView(APIView):
    """
    Тестовая ошибка для проверки Sentry
    """

    def get(self, request):

        raise Exception("Test Sentry Error")