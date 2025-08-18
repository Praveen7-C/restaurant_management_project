from django.test import TestCase
from .models import Customer

# Create your tests here.
class CustomerModelTest(TestCase):
    def test_create_guest_customer(self):
        customer = Customer.objects.create(name="Test Guest", phone="1234567890")
        self.assertEqual(customer.name,"Test Guest")

        
