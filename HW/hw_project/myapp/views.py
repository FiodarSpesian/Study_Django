import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Product, Order

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
    order = Order.objects.filter(customer_id=customer.pk)
    temp = []
    for item in order:
        temp.append(item.products.all(date))
    products = []
    for item in temp:
        for val in item:
            products.append(val)
    return render(request, 'myapp/customer_products.html', {'customer': customer,
                                                            'products': products,
                                                            'count_days': count_days})





