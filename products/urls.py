from django.urls import path

from .views import (
    ProductListView,
    ProductDetailView,
    ProductImportView,
    ProductExportView
)

urlpatterns = [

    path(
        "",
        ProductListView.as_view(),
        name="product-list"
    ),

    path(
        "<int:pk>/",
        ProductDetailView.as_view(),
        name="product-detail"
    ),

    path(
        "import/",
        ProductImportView.as_view(),
        name="product-import"
    ),

    path(
        "export/",
        ProductExportView.as_view(),
        name="product-export"
    ),
]