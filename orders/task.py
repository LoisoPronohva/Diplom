from celery import shared_task

from .services import send_order_confirmation, notify_admin
from .models import Order


@shared_task
def send_order_confirmation_task(order_id):

    order = Order.objects.get(id=order_id)

    send_order_confirmation(order)


@shared_task
def notify_admin_task(order_id):

    order = Order.objects.get(id=order_id)

    notify_admin(order)