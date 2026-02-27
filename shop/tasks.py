from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_invoice_to_admin(order_id, order_details):
    send_mail(
        subject=f"Новый заказ #{order_id}",
        message=f"Детали заказа:\n{order_details}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.DEFAULT_FROM_EMAIL],
    )

@shared_task
def send_order_confirmation(client_email, order_id, order_details):
    send_mail(
        subject=f"Подтверждение заказа #{order_id}",
        message=f"Ваш заказ принят:\n{order_details}",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[client_email],
    )

@shared_task
def import_products_csv(file_path):
    import csv
    from .models import Product, Supplier
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            supplier, _ = Supplier.objects.get_or_create(name=row['supplier'])
            Product.objects.update_or_create(
                name=row['name'],
                supplier=supplier,
                defaults={'price': row['price'], 'attributes': {}}
            )

@shared_task
def export_products_csv(file_path):
    import csv
    from .models import Product
    products = Product.objects.all()
    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['name', 'supplier', 'price'])
        for p in products:
            writer.writerow([p.name, p.supplier.name, p.price])