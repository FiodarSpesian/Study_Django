from django.core.management.base import BaseCommand
from myapp.models import User


class Command(BaseCommand):
    help = "Generate fake users"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of users')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            user = User(name=f'User_{i}', email=f'mail{i}@mail.ru',
                        phone=f'phone_{i}', adress=f'adress_{i}')
            user.save()
