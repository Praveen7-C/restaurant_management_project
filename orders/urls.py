from django.urls import path
from .views import CustomerListCreateView, OrderCreateView, CustomerListCreateView

urlpatterns = [
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('orders/create/', OrderCreateView.as_view(), name='order-create')
    path('Orders/CustomerOrderListView().as_view()', name='customer-orders'), 
]