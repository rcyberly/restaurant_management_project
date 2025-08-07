from django.db import models

# Create your models here.
class Restaurant(object):
    def'__init__'(self, name = "THE NORTSOUT RESTAURANT", slogan = "TASTE CONNECTS FROM NORTH TO SOUTH"):
        self.name = "THE NORTSOUT RESTAURANT"
        self.slogan = "TASTE CONNECTS FROM NORTH TO SOUTH"
    def save(self,instance):
        f{"SAVING RESTAURANT NAME '{self.name}' TO DATABASE "}
        restaurant_instance = Restaurant.name("THE NORTSOUT RESTAURANT")
        restaurant_instance.save()



