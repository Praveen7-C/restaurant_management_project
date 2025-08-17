from django.urls import path
from .views import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name= 'home'),
    path('about/', views.about_view, name='about_us'),
    path('contact/', views.contact_views, name='contact'), 
]