from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerServiceView.as_view(), name='customer-service'),
    path('send-customer-request', views.CustomerRequestSentView.as_view(), name='customer-request-sent')
]