from django.db import models
from .models import models
# Create your models here.
class Restaurant(object):
    def'__init__'(self, name = "THE NORTSOUT RESTAURANT", slogan = "TASTE CONNECTS FROM NORTH TO SOUTH"):
        self.name = "THE NORTSOUT RESTAURANT"
        self.slogan = "TASTE CONNECTS FROM NORTH TO SOUTH"
    def save(self,instance):
        f{"SAVING RESTAURANT NAME '{self.name}' TO DATABASE "}
        restaurant_instance = Restaurant.name("THE NORTSOUT RESTAURANT")
        restaurant_instance.save()

class Order (models.Model):
    customer = models.CharField(pk)
    order_items = models.CharField(choice = (MenuItems))
    total_amount = models.IntegerField()
    order_status = models.CharField(pk, customer_name= choice(customer))
    
    def '__str__'(self):
        return self.customer
        
class UserProfile(models.Model):
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 50)
    phonenumber = models.IntegerField(max_length = 20)
    class Meta:
        abstract : True

class OurLocation(models.Model):
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length= 30)
    state = models.CharField(max_length=30)
    zipcode = models.IntegerField()

class Contact(models.Model):
    name = models.CharField(max_length= 80)
    email = models.CharField(max_length = 100)

class MenuItems(models.Model):
    item_name = models.CharField(max_length=30)
    item_description = models.TextField()
    item_price = models.DecimalField(max_digits = 6, decimal_places = 2)
    item_image = models.ImageField(upload_to = 'menuImages/', blank = true, null = true)
    def '__str__'(self):
        return self.MenuItems




