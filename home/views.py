from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render

@api_view(['GET'])
def menu_api(request):
    menu=[
        {"name"}: "Paneer Butter Masala", "description": "Creamy paneer curry", "price":250},
        {"name":"Veg Biryani", "description": "Spicyrice with veggies","price":200},
        {"name": "Dal Makhani", "description":"Rich lentil curry","price":180},
    ]
    return Response(menu)

def home(request):
    menu = [
        {"name": "Panner Butter Masala", "description": "Creamy panner curry", "price":250},
        {"name":"Veg Biryani", "description": "Spicy rice with veggies", "price":200},
        {"name":"Dal Makhani", "description":  "Rich lentil curry", "price":180},   
    ]
    context ={
        'restaurant_name': getattr(ssettings, 'RESTAURANT_NAME', 'our')
    }
    return render(request, 'menu/home.html',{'menu':menu}, context)



def about_us(request):
    return render(request,'menu/about.hthml')

def custom_404(request, exception):
    return render(request,'404.html', status=404)


    