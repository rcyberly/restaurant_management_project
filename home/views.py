from django.shortcuts import render, request
from django.db import models
from django.contrib import messages
import datetime
from .models import MenuItems
from .serializers import MenuItemsSerializers
from django.core.mail import send_mail
from .forms import ContactForm
from .models import Cart, CartItem

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

    def aboutus_restaurnat_info(request):
        about_restaurant = {
            'name' : 'THE NORTH-SOUTH RESTAURANT',
            'History' : 'When we planned to open a small Food Corner in Neeladhri Bangalore we Found we started to sell Idli , Dosa and Sambar we found it is selling in ample amount,\n Once we tried to keep Rajmah-Rice and KidneyBeans we found that there was a plenty of sale then Makki-di-Roti and Sarson da Sag, we found that The punjabis who lived in Vellore premise of bangalore started to eat and Then we started to keep Hyderabadi Biryani but veg, Then Payasam of Tamil Nadu and Kerala Dishes like utthapam, we found there was a huge sale and By this sale we decided to open Restaurant by the name of THE NORTH-SOUTH RESTAURANT',
            'Mission' : 'Our mission is to keep our Customer happy be That Customer a Poor , Rich or whatever type of Customer he is after all Customer is Customer for us, Keeping in that view we do not compromise with taste and Qaulity',
        }
        return render(request, 'home/aboutus-restaurnat.html'{'restaurant': about_restaurant})

    
    def contact_form_view(request):
        if request.method == 'POST':
            form = contact_form_view('POST')
            if form_is_valid:
                form.cleaned_data['email']
                form.cleaned_data['message']
            else:
                form.contact_form_view()
                return render
        return render(request, 'home/homepage.html', {'form':form})

    def frequently_asked_questions(request):
        faqs = [
            {
                'Question' : 'How do i place an order ?',
                'Answer' : 'To place an order you can see menu item and their price first and then click on button to place an order',

            }
            {
                'Question': 'What are the menu items you serve ?',
                'Answer' : 'We serve authentic Dishes eaten in Tamil , Mallayallam , Kannadda , Telegu , Maharashtrian dishes, Punjabi and North and South indian Dishes',
            }
        ]

        context9 = {
            'faqs': faqs
        }
        return render(request, 'home/homepage.html', context9)

                

        
        