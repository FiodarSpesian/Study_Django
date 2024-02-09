from django.core.management.base import BaseCommand
from random import randint
from myapp.models import Order, User, Product


class Command(BaseCommand):
    help = "Generate fake orders"

    def add_arguments(self, parser):
        parser.add_argument('user_id', type=int, help='Id of user')
        parser.add_argument('product_id', type=int, help='Id of product')

    def handle(self, *args, **kwargs):
        customer = User.objects.filter(pk=kwargs.get('user_id')).first()
        product_id = kwargs.get('product_id')
        product = Product.objects.filter(pk=product_id).first()
        total_price = getattr(Product.objects.filter(pk=product_id).first(), "price")
        order = Order(customer=customer, total_price=total_price)
        order.save()