from django.urls import path
from .views import *

urlpatterns = [
    path('menu/', menu_api, name='menu_api'),
    path('',home, name= 'home'),
]