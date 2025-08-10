from django.urls import path
from .views import *

urlpatterns = [
    path('api/menu/', menu_api, name='menu_api'),
    path('',home, name= 'home'),
    path('about/', about_us, name='about_us'),
    path('staff/login/', staff_login, name='staff-login')
]