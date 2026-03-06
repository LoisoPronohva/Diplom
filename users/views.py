from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Address
from .serializers import RegisterSerializer, AddressSerializer


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer


class AddressListCreateView(generics.ListCreateAPIView):

    serializer_class = AddressSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Address.objects.filter(user=self.request.user)

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


class AddressDeleteView(generics.DestroyAPIView):

    serializer_class = AddressSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        return Address.objects.filter(user=self.request.user)