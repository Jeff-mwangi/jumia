from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import JsonResponse
import json

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
    model = Customer
    form_class = Customer
    template_name = 'register.html'
    success_url = reverse_lazy('login')

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

def updateProduct(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('productId:', productId)

    customer = request.user.customer
    product = requests
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    product = requests.get(f'https://dummyjson.com/products/{productId}').json()
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete() 
    return JsonResponse('Item was added', safe=False)

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             # log in the user
#             user = form.get_user()
#             login(request, user)
#             return redirect('home')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')


