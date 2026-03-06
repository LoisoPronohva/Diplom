from django.urls import path
from .views import ProductListCreateView, ProductSpecificationListCreateView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list'),
    path('specifications/', ProductSpecificationListCreateView.as_view(), name='product-specifications'),
]