from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic.base import TemplateView

import stripe
import json

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'home.html'

def success_view(request):
    session_id = request.GET['session_id']
    stripe.api_key = settings.STRIPE_SECRET_KEY
    checkout_data = stripe.checkout.Session.retrieve(session_id)

    with open('checkout_data.json', 'w') as f:
        json.dump(checkout_data, f)

    return render(request, 'success.html')    

class CancelledView(TemplateView):
    template_name = 'cancelled.html'

@csrf_exempt
def stripe_config(request):
	if request.method == 'GET':
		stripe_config = {'publicKey':settings.STRIPE_PUBLISHABLE_KEY}
		return JsonResponse(stripe_config, safe=False)

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
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'quantity': quantity,
                        'price': 'price_1HIUhDEDp44wgAg5KQlkePWK'
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
            