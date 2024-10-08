from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import login,logout,get_user_model
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import Http404

from django.utils import timezone
from .models import *
from .backends import authenticate

User = get_user_model()

def homepage_view(request):
    foods = Food.objects.filter(active=True)[:9]
    # print(dir(request.user))
    categories = Category.objects.all()
    context = {'foods':foods,'categories':categories}
    return render(request,'index.html',context)

def food_detail_or_order_view(request,food_id):
    food = get_object_or_404(Food,food_id=food_id)
    order = Order.objects.get(food=food)
    print(request.GET)
    end_time = order.timestamp + timezone.timedelta(days=1)
    context = {
        'food':food,
        'time':end_time
    }
    return render(request,'order.html',context)

def search_view(request):
    query = request.GET.get('q','')
    if query:
        foods = Food.objects.filter(Q(name__icontains=query)|Q(category__name__icontains=query))
    context = {
        'query':query,
        'foods':foods
    }
    return render(request,'food-search.html',context)

def category_view(request):
    category = request.GET.get('category','')
    foods = Food.objects.filter(category__name__icontains=category)
    context = {'foods':foods,'category':category}
    return render(request,'category-foods.html',context)

def all_category_view(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'categories.html',context)

def all_foods_view(request):
    foods = Food.objects.filter(active=True)
    context = {
        'foods':foods
    }
    return render(request,'foods.html',context)

@login_required(login_url='login')
def ordering_view(request,food_id):
    food = get_object_or_404(Food,food_id=food_id)
    if request.method == 'POST':
        quantity = request.POST['qty']
        fill_name = request.POST['full-name']
        email = request.POST['email']
        phone_number = request.POST['contact']
        address = request.POST['address']
        order = Order.objects.create(
            food=food,
            quantity=quantity,
            full_name=fill_name,
            phone_number=phone_number,
            email=email,
            address=address
        )
        # cancel = request.POST.get('action')
        # if cancel == 'list':
        #     request.user.profile.foods.remove(food)
        request.user.profile.foods.add(food)
        return redirect(request.META.get('HTTP_REFERER'))

def remove_order_view(request,food_id):
    if request.method == 'POST':
        order = get_object_or_404(Order,food__food_id=food_id)
    elif request.method == 'GET':
        raise Http404
"""
Authentication Signup,Login,Logout Views
"""
def login_view(request):
    if request.method == 'POST':
        obj =  request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=obj,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'credencials error')
            return redirect('login')
    context = {}
    return render(request,'auth/login.html',context)

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if len(password) < 8:
            messages.error(request,'Password must be 8 character or more')
            return redirect('signup')
        if User.objects.filter(Q(username=username)|Q(email=email)).exists():
            messages.error(request,'user already exists')
            return redirect('signup')
        if username and password is not None or not "":
            User.objects.create_user(username=username,email=email,password=password)
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Error')
                return redirect('signup')
    context = {}
    return render(request,'auth/signup.html',context)

def logout_view(request):
    if request.user.is_anonymous:
        return redirect('login')
    logout(request)
    return redirect('home')