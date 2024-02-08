import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'myapp/index.html', )


def about(request):
    logger.debug('About page accessed')
    return render(request, 'myapp/about.html')


def products(request):
    logger.info("Products page accessed")
    return
