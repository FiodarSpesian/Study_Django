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
        price = getattr(product, "price")
        order = Order(customer=customer, total_price=price)
        # users = User.objects.filter(email__in=emails)
        # instance = Setupuser.objects.create(organization=org)
        #
        # instance.emails_for_help.set(users)

        # for i in range(1, count + 1):
        #     user = User(name=f'User_{i}', email=f'mail{i}@mail.ru',
        #                 phone=f'phone_{i}', adress=f'adress_{i}')
        order.save()
