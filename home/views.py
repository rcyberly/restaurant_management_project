from django.shortcuts import render, request
from django.db import models
from django.contrib import messages
import datetime
from .models import MenuItems
from .serializers import MenuItemsSerializers


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

    def reservation_page_view(request):
        if request.method =='POST':
            form = reservation_page_view(request.POST)
            if form_is_valid():
            try:
                context = {
                    'name':name,
                    'email':email,
                    'contactno':contactno,
                }
                form_reservations.save()
                message.success(request,'your form has been saved')
            except:
                if error:
                    message.error(request,'there may have been some error ')
        else:
            form = reservation_page_view()
        return render(request, 'home/Reservation_page.html', context)

    def customer_feedback_view(request):
        if request.method =="POST":
            form = customer_feedback_view(request.POST)
            if form.form_is_valid():
                form.save()
                message.success = (request,'form data has been saved')
            else:
                form = FeedbackForm()
                success = request.GET.get(submitted)==True
        return render(request, 'home/customer_feedback.html', {'form':form,'sucess':success} )

    def footer_page_view(request):
        context1 = {
            
            'date_time' : datetime.datetime.now(),
        }
        return render (requst, 'home/footer.html' context1)


    def 

    def MenuItemsSerializersAPI(self, ListAPI):
        queyset = MenuItems.objects.filter(is_available = True)
        name = NameSerializer()
        description = DescriptionSerializer()
        price = PriceSerializer()

    
        


                

        
        