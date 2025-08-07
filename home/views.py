from django.shortcuts import render, request
from django.db import models

# Create your views here.
def homepageview (request):
    try:
        Restaurant_from_db = Restaurant.objects,first()
        Restaurnat_name = Restaurant.objects.name()
        Restaurant_slogan = Restaurant.objects.slogan()
    except:
        Restaurnat_name = Restaurnat_name
        Restaurant_slogan = 
        
    return(request, homepageview, context)   