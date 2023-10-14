from django.core.mail import BadHeaderError
from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from templated_mail.mail import BaseEmailMessage
from rest_framework.views import APIView
from .tasks import notify_customers
import requests
import logging

logger = logging.getLogger(__name__)


# sending messages
def say_hello(request):
    try:
        message = BaseEmailMessage(
            template_name='emails/hello.html',
            context={'name': 'Friday Onojah'}
        )
        message.send(['friday@sell.com'])

    except BadHeaderError:
        pass
    return render(request, 'hello.html', {'name': 'Hello Dev'})


# runing a background task
# for beat startup celery -A storefront beat
# for celery startup -> celery -A storefront worker --loglevel=info
# flower -> celery -A storefront flower
def notify_customers(request):
    notify_customers.delay('Delivered')
    return render(request, 'hello.html', {'name': 'Hello Dev'})


@cache_page(5 * 60)
def function_cach(request):
    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
    return render(request, 'hello.html', {'name': data['args']})


class CachClass(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        response = requests.get('https://httpbin.org/delay/2')
        data = response.json()
        return render(request, 'hello.html', {'name': 'Mosh'})


class Logger(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            logger.info('Received the response')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'hello.html', {'name': 'Mosh'})
