from django.urls import path
from .views import views

app_name = 'account'

urlpatterns = [
    path('staff-login/', views.staff_login, name='staff_login'),
    path('me/profile/', views.profile_view, name='my-profile'),
]
