from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    #simple hardcoded menu
    path('menu/simple/', views.simple_menu, name='simple-menu'),

    #Restaurants CRUD
    path('restaurants/', views.restaurant_list_create, name='restaurant-list-create'),
    path('restaurants/<int:pk>/', views.restaurant_detail, name='restaurant-detail'),

    #MenuItem CRUD
    path('menuitems/', views.menuitem_list_create, name='menuitem-list-create'),
    path('menuitems/<int:pk>/', views.menuitem_detail, name='menuitem-detail'),
]