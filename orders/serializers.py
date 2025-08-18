from rest_framework import serializers
from .models import Customer, Order
from products.models import MenuItem
from products.serializers import MenuItemSerializer

# Task-18: Customer Serializer (all fields optional)
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'email', 'created_at']


# Serializer for order creation
class OrderCreateSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(required=False)
    items = serializers.PrimaryKeyRelatedField(
        queryset=MenuItem.objects.all(), many=True
    )

    class Meta:
        model = Order
        fields = ['id', 'customer', 'restaurant', 'items', 'total_amount', 'status', 'created_at']

    def create(self, validated_data):
        request = self.context.get('request')
        customer_data = validated_data.pop('customer', None)
        items = validated_data.pop('items')

        # Authenticated user
        if request and request.user.is_authenticated:
            validated_data['customer_user'] = request.user
        else:
            # Guest -> create customer record if provided
            if customer_data:
                customer = Customer.objects.create(**customer_data)
                validated_data['customer'] = customer

        order = Order.objects.create(**validated_data)
        order.items.set(validated_data['items'])
        return order


# Task-23: Lightweight Order listing serializer
class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'status', 'total_amount', 'created_at']
