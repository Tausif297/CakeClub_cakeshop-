from django.db import models
from django.shortcuts import render
from products.models import Products

def index(request):
    cake = Products.objects.all()
    return render(request,'index.html',{'cake':cake})

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'login.html')



