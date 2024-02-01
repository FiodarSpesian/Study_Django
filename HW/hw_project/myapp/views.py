import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)


def index(request):
    logger.info('Index page accessed')
    return render(request, 'index.html', )


def about(request):
    logger.debug('About page accessed')
    return render(request, 'about.html')


# def about(request):
#     return HttpResponse("About us")
