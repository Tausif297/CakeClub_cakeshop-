from django.contrib import admin
from django.db import models
from .models import Orders, Products
# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','name','price','desc']

class OrdersAdmin(admin.ModelAdmin):
    list_display=['order_id','items_json','name','phone_no','email','address','city','state','zip_code']

admin.site.register(Products,ProductsAdmin)
admin.site.register(Orders,OrdersAdmin)