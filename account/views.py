from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, UserSerializer
from .models import Profile

@api_view(['POST'])
@permission_classes([AllowAny])
def staff_login(request):
    """
    Staff login via email and password.
    Request payload: { "email": "staff@example.com", "password": "pass" }
    Returns basic user info on success.
    """
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        return Response({"detail": "Email and password required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(email__iexact=email)
    except User.DoesNotExist:
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    if not user.check_password(password):
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)

    # Optionally ensure they are staff (restaurant staff)
    # If you want to restrict to staff only, uncomment the following:
    # if not user.is_staff:
    #     return Response({"detail": "User is not staff."}, status=status.HTTP_403_FORBIDDEN)

    serializer = UserSerializer(user)
    return Response({"status": "success", "user": serializer.data})

@api_view(['GET', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    """
    GET -> view profile
    PUT/PATCH -> update profile fields (full_name, phone_number)
    """
    profile = getattr(request.user, 'profile', None)
    if profile is None:
        profile = Profile.objects.create(user=request.user)

    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    # update
    serializer = ProfileSerializer(profile, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
