from django.urls import path
from .views import *

urlpatterns = [
    path('login', staff_login,name='staff_login'),
]
