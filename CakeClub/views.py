from django.db import models
from django.shortcuts import render
from products.models import Products
import random
def index(request):
    cake = Products.objects.raw('select * from Products_products order by rand() limit 8')
    return render(request,'index.html',{'cake':cake})

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')



