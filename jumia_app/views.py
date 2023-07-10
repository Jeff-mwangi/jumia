from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import *
import requests

def index (request):
    products = requests.get('https://dummyjson.com/products').json()
    return render(request, 'store/home.html', {'products': products})

def product_detail(request, pk):
    product = requests.get(f'https://dummyjson.com/products/{pk}').json()
    return render(request, 'store/product_detail.html', {'product': product})

def cart (request):
    return render (request, 'store/cart.html')

class Registration(CreateView):
    model = User
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    fields = ['username', 'email', 'phone_number', 'address', 'password1', 'password2']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class ShippingAddress(CreateView):
    model = ShippingAddress
    template_name = 'checkout.html'
    success_url = reverse_lazy('home')
    fields = ['address', 'city', 'state', 'zipcode']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

