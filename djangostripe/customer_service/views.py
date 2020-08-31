from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomerService

import stripe
import json

from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class CustomerServiceView(CreateView):
	model = CustomerService
	fields = ['title', 'content']

# Create your views here.
class CustomerRequestSentView(TemplateView):
	template_name = 'customer_service/customer_request_sent.html'

@csrf_exempt
def create_checkout_session(request):
    if request.method == 'POST':
        quantity = json.loads(request.body)['quantity']
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            checkout_session = stripe.checkout.Session.create(
                billing_address_collection='auto',
                shipping_address_collection={'allowed_countries': ['US', 'CA'],},
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + '',
                payment_method_types=['card', 'alipay'],
                mode='payment',
                line_items=[
                    {
                        'quantity': quantity,
                        'price': 'price_1HIUhDEDp44wgAg5KQlkePWK'
                    },
                    {
                        'quantity': 1,
                        'price': 'price_1HIMkfEDp44wgAg5VZWwWt9S'
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

"""
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
"""
            