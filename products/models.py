from django.db import models
from django.conf import settings

# Create your models here.
Class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    address = models.TextField(Blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete= models.CASCADE,related_name='menu_items')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.restaurant.name}"