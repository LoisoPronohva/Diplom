from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order
from .tasks import send_order_confirmation_task, notify_admin_task


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):

    if created:

        send_order_confirmation_task.delay(instance.id)

        notify_admin_task.delay(instance.id)