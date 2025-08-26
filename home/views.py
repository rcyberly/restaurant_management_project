from django.shortcuts import render, request
from django.db import models
from django.contrib import messages
import datetime
from .models import MenuItems
from .serializers import MenuItemsSerializers
from django.core.mail import send_mail
from .forms import ContactForm


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


    def our_location_view(request):
        try:
            restaurant_info = Restaurant.objects.first()
        except Restaurant.DoesNotExist
        restaurnat_info = None
        context2 = {
            'restaurant': restaurnat_info
        }
        return render(request, 'home/homepage.html', context2)

    def menupage_view(request):
        try:
            restaurant_menu = Restaurant.objects.filter.MenuItems()
        except MenuItems.DoesNotExist
        context3 = {
            'restaurant_menu' : restaurant_menu
        }
        return render(request, 'home/menupage.html', context3)

    def MenuItemsSerializersAPI(self, ListAPI):
        queyset = MenuItems.objects.filter(is_available = True)
        name = NameSerializer()
        description = DescriptionSerializer()
        price = PriceSerializer()

    def Resturant_working_view*(self):
        restaurnat_working = RestaurantOpeningHours.objects.all()
        if restaurant_working == 'Sunday':
            return f{"SUNDAY : 10:00 AM TO 21:00 PM"}
        elif:
             return f{"MONDAY : 11:00 AM TO 23:00 PM "}
        elif:
            return f{"TUESDAY : 11:00 AM TO 23:00 PM "}
        elif:
            return f{"WEDNESDAY : 11:00 AM TO 23:00 PM "}
        elif:
            return f{"THURSDAY : 11:00 AM TO 23:00 PM"}
        elif:
            return f{"FRIDAY : 11:00 AM TO 23:00 PM "}
        elif: 
            return f{"SATURDAY : 11:00 AM TO 23: 00 PM "}
        context4 = {
            'restaurant_working': restaurnat_working
        }
    return render(request, 'home/homepage.html', context4)

    def Menuitem_view (request):
        Menuitem = MenuItem.objects.all()
        context5 = {
            'name_of_item': name_of_item,
            'description_of_item': description_of_item,
            'price_of_item': price_of_item,
            'image_of_item' : image_of_item,
            
        }
    return render(request, 'home/homepage.html', context5)


    def homepage_search_view(request):
        if request.method =='POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                send_mail = (
                    f"New Contact Form Submission : {subject}",
                    f"Form:\n{name}\n\nemail:{email}\n\n\n{message}",
                    settings.EMAIL_HOST_USER,
                    ['emailidrest@example.com'],
                    fail_sliently = False,
                )
            else:
                form = ContactForm()
            return render(request, 'home/contactus.html', {'form':form})

    def homepage_search_view(request):

        search_query = request.GET.get('a','')

        if search_query:
            menu_items = MenuItems.objects.filter(name__icontains = search_query)
        else:
            menu_items = MenuItems.objects.all()
        context6 = {
            'menu_items':menu_items,
            'search_query':search_query,
        }
        return render(request, 'home/homepage.html',context6)

    def restaurant_phone_number(request):

        phone_number = RestaurantPhoneNumber.objects.all()

        context7 = {
            restaurant_phone_number' : restaurant_phone_number
        }

        return render(request, 'home/homepage.html', context7)
        
    def restaurna_image_view(request):

        restaurant_image = RestaurnatImage.objects.all()
        context8 = {
            'restaurant_image' : restaurnat_image
        }
        return render(request,'home/homepage.html', context8)
    
        


                

        
        