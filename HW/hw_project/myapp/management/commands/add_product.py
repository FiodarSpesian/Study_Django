from random import choices
from django.core.management.base import BaseCommand
from myapp.models import Product

DESCRIPTION = "Lorem ipsum dolor sit amet, consectetur adipisicingelit." \
              "consequuntur cumque, delectus et illo iste maxime" \
              "nihil non nostrum odio officia, perferendis placeat quasi quibusdam quisquam quod sunt " \
              "tempore temporibus ut voluptatum? A aliquam culpa ducimus, eaque eum illo mollitia nemo " \
              "tempore unde vero! Blanditiis deleniti ex hic, laboriosam maiores odit officia praesentium " \
              "quae quisquam ratione, reiciendis, veniam. Accusantium assumenda consectetur consequatur " \
              "consequuntur corporis dignissimos ducimus eius est eum expedita illo in, inventore " \
              "ipsum iusto maiores minus mollitia necessitatibus neque nisi optio quasi quo quod, " \
              "quos rem repellendus temporibus totam unde vel velit vero vitae voluptates."


class Command(BaseCommand):
    help = "Generate fake products"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count of products')

    def handle(self, *args, **kwargs):
        text = DESCRIPTION.split()
        count = kwargs.get('count')
        for i in range(1, count + 1):
            product = Product(name=f'Product_{i}', description=' '.join(choices(text, k=12)),
                              price=i, count=20)
            product.save()
