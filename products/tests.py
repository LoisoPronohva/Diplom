from django.test import TestCase

from .models import Product


class ProductTest(TestCase):

    def test_create_product(self):

        product = Product.objects.create(

            name="Phone",

            price=1000,

            stock=10

        )

        self.assertEqual(product.name, "Phone")