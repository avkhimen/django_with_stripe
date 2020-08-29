from django.urls import path
from . import views

urlpatterns = [
    path('', views.CustomerServiceView.as_view(), name='customer-service'),
]