from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    return render(request, 'ecommerce_app/index.html')

def login(request):
    return render(request, 'ecommerce_app/login.html')

def cart(request):
    return render(request, 'ecommerce_app/cart.html')

def dashboard(request):
    return render(request, 'ecommerce_app/dashboard.html')

def borrower(request):
    return render(request, 'ecommerce_app/borrower.html')
