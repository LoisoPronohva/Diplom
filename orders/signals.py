from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Order

# Файл в репо называется task.py — импортируем из него
from .task import send_order_confirmation_task, notify_admin_task


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):
    if created:
        try:
            # В локальной разработке брокера Celery может не быть — защищаем вызов
            send_order_confirmation_task.delay(instance.id)
            notify_admin_task.delay(instance.id)
        except Exception:
            # В проде замените на логирование
            pass