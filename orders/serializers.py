from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderItem

        fields = (
            "id",
            "product",
            "quantity",
            "price",
        )


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(many=True)

    class Meta:

        model = Order

        fields = (
            "id",
            "user",
            "delivery_address",
            "status",
            "created_at",
            "items",
        )

        read_only_fields = (
            "status",
            "created_at",
        )

    def create(self, validated_data):

        items_data = validated_data.pop("items")

        order = Order.objects.create(**validated_data)

        for item_data in items_data:

            OrderItem.objects.create(
                order=order,
                **item_data
            )

        return order

    def update(self, instance, validated_data):

        items_data = validated_data.pop("items", None)

        instance.delivery_address = validated_data.get(
            "delivery_address",
            instance.delivery_address
        )

        instance.save()

        if items_data:

            instance.items.all().delete()

            for item_data in items_data:

                OrderItem.objects.create(
                    order=instance,
                    **item_data
                )

        return instance