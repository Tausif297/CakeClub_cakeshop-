from django.contrib import admin
from .models import Contact,Register

class RegisterAdmin(admin.ModelAdmin):
    list_display=['id','name','Phone','Email','Password']

class ContactAdmin(admin.ModelAdmin):
    list_display=['id','name','mobile','email','textmsg']

admin.site.register(Contact,ContactAdmin)
admin.site.register(Register,RegisterAdmin)