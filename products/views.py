from django.shortcuts import render
from .models import Orders, Products
from django.contrib import messages
# Create your views here.
def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('items_json')
        name=request.POST.get('name')
        phone_no=request.POST.get('phone_no')
        email=request.POST.get('email')
        address=request.POST.get('address1')+ '' +request.POST.get('address2')
        city=request.POST.get('city')
        state=request.POST.get('state')
        zip_code=request.POST.get('zip_code')
        if len(phone_no) !=10:
            messages.error(request,"Please enter 10 digit valid number")
        # elif type(mobile) != int:
        #     messages.error(request,"Charecters not allowed")
        else:
            order=Orders(items_json=items_json,name=name,phone_no=phone_no,email=email,address=address,city=city,state=state,zip_code=zip_code)
            order.save()
            messages.success(request,"Your Order Is Placed Thanks For Order. Shop More Stay Safe Stay Happy")
    return render (request, 'checkout.html')

def cake(request):
    cake = Products.objects.all()
    return render(request,'product.html',{'cake':cake})
