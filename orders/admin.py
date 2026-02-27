from django.contrib import admin
from .models import Order, OrderItem
from shop.tasks import send_invoice_to_admin, send_order_confirmation

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'status', 'created_at')
    actions = ['mark_as_completed']

    def mark_as_completed(self, request, queryset):
        for order in queryset:
            order.status = 'completed'
            order.save()
            send_invoice_to_admin.delay(order.id, str(order.items.all()))
            send_order_confirmation.delay(order.client.email, order.id, str(order.items.all()))
    mark_as_completed.short_description = "Отметить как выполненный"

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')