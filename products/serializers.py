from rest_framework import serializers

from .models import Product, ProductSpecification


class ProductSpecificationSerializer(serializers.ModelSerializer):

    class Meta:

        model = ProductSpecification

        fields = (
            "id",
            "key",
            "value",
        )


class ProductSerializer(serializers.ModelSerializer):

    specifications = ProductSpecificationSerializer(
        many=True,
        read_only=True
    )

    class Meta:

        model = Product

        fields = (
            "id",
            "name",
            "description",
            "price",
            "stock",
            "specifications",
        )