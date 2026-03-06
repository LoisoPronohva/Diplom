import csv

from .models import Product


def import_products_from_csv(file):

    decoded_file = file.read().decode("utf-8").splitlines()

    reader = csv.DictReader(decoded_file)

    for row in reader:

        Product.objects.create(

            name=row["name"],

            description=row.get("description", ""),

            price=row["price"],

            stock=row.get("stock", 0)

        )


def export_products_to_csv():

    products = Product.objects.all()

    rows = []

    for product in products:

        rows.append({

            "id": product.id,

            "name": product.name,

            "price": product.price,

            "stock": product.stock

        })

    return rows