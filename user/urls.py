from django.urls import path
from . import views

urlpatterns = [
    path('user/',views.user,name='userproductpage'),
    path('contact/',views.contact,name='contactuspage'),
    path("logout",views.logout2,name="logoutpage"),
    path("login",views.Userlogin,name="login"),
    path("register",views.register,name="registerpage")
]
