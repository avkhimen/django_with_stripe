from django.shortcuts import render
from django.views.generic import CreateView
from .models import CustomerService

# Create your views here.
class CustomerServiceView(CreateView):
	model = CustomerService
	fields = ['title', 'content']