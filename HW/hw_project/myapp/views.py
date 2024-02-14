import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import User, Product, Order
from .forms import ProductFormWidget
from django.core.files.storage import FileSystemStorage  # import нужный для работы с фалами

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
        customer_id=customer_id)  # order_by(date_ordered__gt=f'{datetime.now() - timedelta(days=count_days)}')
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


def add_product(request):
    if request.method == 'POST':
        form = ProductFormWidget(request.POST, request.FILES)
        message = 'Ошибка в данных'
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            count = form.cleaned_data['count']
            image = form.cleaned_data['image']
            logger.info(f'Получили товар: {name=}, {price=}, {count=}.')
            product = Product(name=name, description=description, price=price, count=count, image=image)
            product.save()
            message = 'Пользователь сохранён'
    else:
        form = ProductFormWidget()
        message = 'Заполните форму'
    return render(request, 'myapp/add_product_form.html', {'form': form, 'message': message})
