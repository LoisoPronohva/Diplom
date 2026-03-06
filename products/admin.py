from django.contrib import admin

from .models import Product, ProductSpecification


class ProductSpecificationInline(admin.TabularInline):

    model = ProductSpecification

    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "price",
        "stock",
    )

    inlines = [
        ProductSpecificationInline
    ]


@admin.register(ProductSpecification)
class ProductSpecificationAdmin(admin.ModelAdmin):

    list_display = (
        "product",
        "key",
        "value",
    )