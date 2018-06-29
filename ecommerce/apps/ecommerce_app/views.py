from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
import re
# import stripe


from .models import *
from django.contrib import auth

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

def index(request):
    return render(request, 'ecommerce_app/login.html')

def register(request):
    found_users = User.objects.filter(email =request.POST['email'] )
    error=False
    if len(request.POST['first_name']) < 2:
        messages.error(request,"Name must be greater than two letters")
        error=True
    if len(request.POST['last_name']) < 2:
        messages.error(request,"Last name must be greater than two letters")
        error=True
    if len(request.POST['password'])  <= 8:
        messages.error(request,"Password must be greater than eight characters")
        error=True
    if request.POST['password'] != request.POST['c_password']:
        messages.error(request,"Password confirmation must match")
        error=True
    if len(found_users) > 0:
        messages.error(request,"That email is already registered. Try to sign in!")
        error=True
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.error(request,"Email must be valid")
        error=True
    if error:
        return redirect('/')
    else:
        password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        u = User.objects.create(first_name = request.POST['first_name'],last_name = request.POST['last_name'], email = request.POST['email'], password = password)
        request.session['id'] = u.id
        return redirect('/dashboard')

def login(request):
    user = User.objects.filter( email = request.POST['email'])
    if len(user) > 0:
        user = user[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['id'] = user.id
            return redirect('/dashboard')
        else:
            messages.error(request,"Try again, your email or password is incorrect")
            return redirect('/')
    else:
        messages.error(request,"Try again, your email or password is incorrect")
#         stripe.Charge.retrieve(
#   "ch_1CiBUn2eZvKYlo2CsK0JYKuB",
#   api_key="sk_test_BQokikJOvBiI2HlWgH4olfQ2"
# )
        return redirect('/')

def show_product(request):
    context={
        'products' : Product.objects.all(),
    }
    return render(request,context, 'ecommerce_app/show_product.html')


def process(request):
    return redirect('/login')

def cart(request):
    context={
        'user' : User.objects.filter(id=request.session['id']),
        'products_purchased' : Product.objects.filter(buyers_id = request.session['id']),
    }
    return render(request, 'ecommerce_app/cart.html')

def shopping_process(request):

    return redirect('/dashboard')


def dashboard(request):
    se_user = User.objects.filter( id = request.session['id'])
    u = se_user[0]
    context={
        'products' : Product.objects.all(),
        'user' : User.objects.filter(id = request.session['id']),
        'species' : Species.objects.all()
    }
    return render(request, 'ecommerce_app/dashboard.html',context,u)

def back(request):
    return redirect('/dashboard')

def logout(request):
    auth.logout(request)
    return redirect('/')

def cart(request):
    return render(request,'ecommerce_app/cart.html')

def review(request):
    return render(request,'ecommerce_app/review.html')

def showroom(request):
    return render(request,'ecommerce_app/showroom.html')




# POSSIBLY NEEDED QUERIES!
# User.objects.filter(id = request.session['id'])
# Product.objects.filter(id = product_id)
# u = User.objects.filter(id = request.session['id']) // u.first_name = request.POST['^*input*^'] // Use this to update user data
# >>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<
# Use this code to add a buyer to a products M2M field:
#
# this_buyer = User.objects.get(id=request.session['id'])
# curr_purchase = Product.objects.filter(id=id)[0]
# curr_purchase.buyers.add(this_buyer)
# curr_purchase.save()
# >>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<
