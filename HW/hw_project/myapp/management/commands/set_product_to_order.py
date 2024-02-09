from django.core.management.base import BaseCommand
from random import randint
from myapp.models import Order, User, Product


class Command(BaseCommand):
    help = "Set product by id to order"

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='Id of order')
        parser.add_argument('product_id', type=int, help='Id of product')

    def handle(self, *args, **kwargs):
        order = Order.objects.filter(pk=kwargs.get('order_id')).first()
        product_id = kwargs.get('product_id')
        product = Product.objects.filter(pk=product_id).first()
        order.products.add(product)
        total_price = 0
        products_from_order = order.products.all()  # вывод products по id заказа
        for prod in products_from_order:
            total_price += prod.price
        order.total_price = total_price # надо исправить
        order.save()
        # self.stdout.write(f'{total_price}')
