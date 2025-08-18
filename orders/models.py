from django.db import models
from django.conf import settings
from products.models import MenuItem, Restaurant

# Create your models here.
class Customer(models.model):
    name = models.CharField(max_length=255, blank=True, null =True)
    phone = models.CharField(max_length=20, blank =True, null=True)
    email = models.EmailField(blank=True, null-True)
    created_at = models.DataTimeField(auto_now_add=True)

    def __str__(self):
        return self.name or f"Customer #{self.id}"
        
class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled','Cancelled'),
    ]

    customer_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, blank=True, null=True 
    )
    customer = models.ForeignKey(
        Customer, on_delete= models.SET_NULL, blank=True, null=True
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='orders', null=True, blank=True)
    items = models.ManyToManyField(MenuItem)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default= 'pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.status}"