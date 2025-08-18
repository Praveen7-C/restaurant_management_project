from django.urls import path
from .views import CustomerListCreateView, OrderCreateView, CustomerListCreateView

app_name = 'orders'

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create')
    path('orders/', CustomerOrderListView().as_view()', name='customer-orders'), 
]