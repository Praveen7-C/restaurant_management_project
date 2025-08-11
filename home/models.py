from django.db import models

# Create your models here.
class Resturant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField(blanks=True , null = True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Restaurants"