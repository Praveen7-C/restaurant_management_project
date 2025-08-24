from django.shortcuts import render, get_object_or_404
from products.models import MenuItem, Restaurant
from django.conf import settings

def home_view(request):
    menu_items = []
    items = MenuItem.objects.filter(is_available=True).order_by('created_at')
    if not items:
        menu_items = [
        {"name": "Panner Butter Masala", "description": "Creamy panner curry", "price":250},
        {"name":"Veg Biryani", "description": "Spicy rice with veggies", "price":200},
        {"name":"Dal Makhani", "description":  "Rich lentil curry", "price":180},   
    ]

    else:
        for item in items:
            menu_items.append({
                "name": item.name,
                "description": items.description,
                "price": item.price,
                "is_available": item.is_available
            })

    restaurant_obj = Restaurant.objects.first()
    if restaurant_obj:
        restaurant_name = restaurant_obj.name
        phone_number = restaurant_obj.phone_number or getattr(settings, 'RESTAURANT_PHONE', 'Not available')
    else:
        restaurant_name= getattr(settings, 'RESTAURANT_NAME', 'My Restaurant')
        phone_number = getattr(settings, 'RESTAURANT_PHONE', 'Not available')

    context ={
        "menu_items": menu_items,
        'restaurant_name': restaurant_name,
        'phone_number': phone_number,
    }
    return render(request, 'menu/home.html', context)

#Simple About Us Page.
def about_us(request):
    restaurant_obj = Restaurant.objects.first()
    about_text = {
        f"Welcome to {restaurant_obj.name}. We serve delicious food!"
        "Welcome! We are a small family-run restaurant serving tasty meals."
    }
    context = {
        'about_text': about_text,
        'restaurant_name': restaurant_obj.name if restaurant_obj else getattr(settings, 'RESTAURANT_NAME', 'My Restaurant'),

    }
    return render(request,'menu/about.html', context)

def custom_404(request):
    return render(request,'404.html', status=404)

#simple Contact us page
def contact_view(request):
    restaurant_obj = Restaurant.objects.first()
    restaurant_name = (
        restaurant_obj.name if restaurant_obj else getattr(settings,"RESTAURANT_NAME", 'My Restaurant')
    )
    phone_number = (
        restaurant_obj.phone_number if restaurant_obj else getattr(settings,'RESTAURANT_PHONE', '+91-9876543210')
    )
    email = getattr(settings, 'RESTAURANT_EMAIL', 'contact@example.com')
    address = getattr(settings, 'RESTAURANT_ADDRESS', '123 Main Street, City, Country')

    context = {
        'restaurant_name': restaurant_name,
        'phone_number': phone_number,
        'email': email,
        'address': address,
    }
    return render(request, 'menu/contact.html', context)

    def reservations_view(request):
        context = {
            "message": "Online reservations will be available soon. Please call us to book a table!"
        }
        return render(request, 'menu/reservations.html', context)