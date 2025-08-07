from django.shortcuts import render, request
from django.db import models

# Create your views here.
def homepageview (request):
    try:
        Restaurant_from_db = Restaurant.objects,first()
        name = Restaurant.objects.name()
        slogan = Restaurant.objects.slogan()
    except:
        Restaurnat_name = "THE NORTSOUT RESTAURANT"
        Restaurant_slogan = "TASTE CONNECTS FROM NORTH TO SOUTH"
    context:
        {
            'name' : name,
            'slogan' : slogan 
        }

    
        
    return(request, homepageview, context)   