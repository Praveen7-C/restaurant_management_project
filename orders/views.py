from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Customer, Order
from .serializers import CustomerSerializer, OrderCreateSerializer, OrderListSerializer


# Create your views here.
#Customer list & create
class CustomerListCreateView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        customers = Customer.objects.all().order_by('-created at')
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Order create with auto-customer for guest
class OrderCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            return Response({
                "order_id": order_id,
                "status": "success",
                "customer": CustomerSerializer(order.customer).data if order.customer else None
                }, status= status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#List orders for a customer (guest or logged-in)
class CustomerOrderListView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        customer_id = request.query_params.get('customer_id')
        if request.user.is_authenticated and not customer_id:
            orders = Order.objects.filter(customer_user=request.user)
        elif customer_id:
            orders = Order.objects.filter(customer_id = customer_id)
        else:
            return Response({"detail": "Authentication or customer_id required."}, status=status.HTTP_400_BAD_REQUEST)

            serializer = OrderListSerializer(orders, many=True)
            return Response(serializer.data)


