from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=255)
    Email = models.CharField(max_length=100)
    Password = models.CharField(max_length=14)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name=models.CharField(max_length=255)
    mobile=models.CharField(max_length=255)
    email=models.EmailField()
    textmsg=models.CharField(max_length=500)
    def __str__(self):
        return self.name