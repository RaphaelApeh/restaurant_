from django.shortcuts import render,get_object_or_404
from django.db.models import Q

from .models import *

def homepage_view(request):
    foods = Food.objects.filter(active=True)[:9]
    categories = Category.objects.all()
    context = {'foods':foods,'categories':categories}
    return render(request,'index.html',context)

def food_detail_or_order_view(request,food_id):
    food = get_object_or_404(Food,food_id=food_id)
    context = {
        'food':food
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