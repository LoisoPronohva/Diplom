from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserListView(generics.ListCreateAPIView):
    """
    Получение списка пользователей
    и создание нового пользователя
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    Получение пользователя по ID
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer