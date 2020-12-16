from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm

# Create your views here.
# @login_required(login_url='login')
def welcome(request): 
    return render(request, 'home.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account has been successfully created for ' + user)
                return redirect('login')

        context = {'form':form}
        return render(request, 'accounts/register.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('welcome')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('welcome')
            else:
                messages.info(request, 'Username or password is incorrect')    
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def list_category(request,category_id):
    all_categories  = Product.objects.filter(id = category_id).all()
    return render(request, 'men.html', {"all_categories": all_categories})

def display_product(request):
    all_products = Product.objects.all()
    return render(request, 'product.html', {"all_products": all_products})

def single_product(request,product_id):
    product = Product.objects.get(id = product_id)
    return render(request, 'singleProduct.html', {"product":product})    
 
def store(request):
	context = {}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)
