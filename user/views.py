from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import Contact, Register
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.
def user(request):
    return HttpResponse('kya haal ap to hamare user ho')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        email=request.POST.get('email')
        textmsg=request.POST.get('textmsg')
        if len(mobile) !=10:
            messages.error(request,"Please enter 10 digit valid number")
        # elif type(mobile) != int:
        #     messages.error(request,"Charecters not allowed")
        else:
            contact=Contact(name=name,mobile=mobile,email=email,textmsg=textmsg)
            contact.save()
            messages.success(request,"Your message has been sent.")

    return render(request,"contact.html")

def register(request):
    if request.method =='POST':
        name=request.POST.get('name')
        Phone=request.POST.get('Phone')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        if len(Phone) !=10:
            messages.error(request,"Please enter 10 digit valid number")
        else:
            try:
                myuser=User.objects.create_user(name,Email,Password)
                myuser.save()
                registeruser=Register(name=name,Phone=Phone,Email=Email,Password=Password)
                registeruser.save()
                messages.success(request,"You have been registered as a user")
                return redirect('/')
            except Exception:
                messages.error(request,"Userr_name already exists")
    return render(request,'register.html')

def Userlogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('/')
        else:
            messages.success(request,"Incorrect Data ! please try again")
            return redirect('/login')

def logout2(request):
    logout(request)
    messages.success(request,"You are logged out")
    return redirect("/")