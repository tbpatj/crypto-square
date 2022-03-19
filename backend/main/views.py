from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

#Register function
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(**request.data.dict())
    auth.login(request, user)
    return Response(f"Successful Registration. {request.data['username']} logged in.")

#Login Function
def login(request):
    user = auth.authenticate(username=request.data['username'], password=request.data['password'])
    if(user is not None):
        auth.login(request, user)
        return Response(f"{user.username} is logged in.")
    else:
        return Response("Invalid username or password.", status=status.HTTP_403_FORBIDDEN)

#Logout Function
@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response("User is logged out.")