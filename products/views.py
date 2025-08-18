from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Restaurant, MenuItem
from .serializers import RestaurantSerializer, MenuItemSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
@permission_classes([AllowAny])
def simple_menu(request):
    menu = [
        {"name": "Paneer Butter Masala", "description": "Creamy paneer in buttery tomato gravy.", "price": "250.00"},
        {"name": "Margherita Pizza", "description": "Classic cheese & tomato pizza.", "price": "350.00"},
        {"name": "Veg Biryani", "description": "Aromatic basmati rice with mixed vegetables.", "price": "200.00"},
    ]
    return Response({"menu": menu})



@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def restaurant_list_create(request):
    if request.method == 'GET':
        qs = Restaurant.objects.all().order_by('-created_at')
        serializer = RestaurantSerializer(qs, many=True)
        return Response(serializer.data)

    # POST
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)

    if request.method == 'GET':
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    restaurant.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['POST', 'GET'])
@permission_classes([AllowAny])
def menuitem_list_create(request):
    if request.method == 'GET':
        restaurant_id = request.query_params.get('restaurant_id')
        qs = MenuItem.objects.all().order_by('-created_at')
        if restaurant_id:
            qs = qs.filter(restaurant_id=restaurant_id)
        serializer = MenuItemSerializer(qs, many=True)
        return Response(serializer.data)

    # POST
    serializer = MenuItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def menuitem_detail(request, pk):
    item = get_object_or_404(MenuItem, pk=pk)

    if request.method == 'GET':
        serializer = MenuItemSerializer(item)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = MenuItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    item.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
