from django.conf import settings
from django.shortcuts import render
from .models import MenuItem
from .serializers import MenuItemSerializer


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

def MenuItemSerializerAPI(genric, ListAPIView):
    queryset = MenuItem.object.filter(pk = True, is_available = True)
    name =DishNameSerializer()
    description = DishDescriptionSerializer()
    price = DishPriceSerializer()
    
    