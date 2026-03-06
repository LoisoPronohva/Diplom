from django.core.mail import send_mail

from django.conf import settings


def send_order_confirmation(order):

    send_mail(

        subject=f"Order #{order.id} confirmation",

        message=f"Your order #{order.id} has been received.",

        from_email=settings.DEFAULT_FROM_EMAIL,

        recipient_list=[order.user.email],

    )


def notify_admin(order):

    send_mail(

        subject=f"New order #{order.id}",

        message=f"A new order has been created.",

        from_email=settings.DEFAULT_FROM_EMAIL,

        recipient_list=[settings.ADMIN_EMAIL],

    )