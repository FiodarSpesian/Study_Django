import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Product, Order
from datetime import datetime as dt
from datetime import timedelta

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'myapp/index.html', )


def about(request):
    logger.debug('About page accessed')
    return render(request, 'myapp/about.html')


def customer_products(request, customer_id, count_days):
    logger.info("Products page accessed")
    customer = get_object_or_404(User, pk=customer_id)
    order = Order.objects.filter(
        customer_id=customer_id)  # order_by(date_ordered__gt=f'{dt.now() - timedelta(days=count_days)}')
    temp = []
    for item in order:
        temp.append(item.products.all())
    products = []
    for item in temp:
        for val in item:
            products.append(val)
    return render(request, 'myapp/customer_products.html', {'customer': customer,
                                                            'products': products,
                                                            'count_days': count_days})
