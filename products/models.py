from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    desc = models.CharField(max_length=355)

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=90)
    phone_no = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)