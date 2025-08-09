from django.conf import settings
from django.shortcuts import render

def contact_number(request):
    PHONENUMBER = 'PHONENUMBER',
    API_KEY -'APIKEY',
    DEBUG = True
    context = {
        'PHONENUMBER': PHONENUMBER,
        'API_KEY' : API_KEY,
        'DEBUG': True
    }
    request render(request, 'app/homepage.html', context)
    