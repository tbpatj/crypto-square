from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User

from rest_framework import status
from django.http import HttpResponse
from .models import Merchant

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
def test(request):
    current_user = request.user
    print(current_user.id)
    return HttpResponse("yup")

@api_view(['POST'])
def exists_username(request):
    return Response(auth.get_user_model().objects.filter(username=request.POST['email']))


#Register function
@api_view(['POST'])
def register(request):
    data = request.data
    body = {"username":data['username'], "email":data['email'],"first_name":data['first_name'], "last_name":data['last_name']}
    user = User.objects.create_user(body)
    auth.login(request, user)
    #Create a merchant linked model
    merchant = Merchant(user_id=user.id,stripe_id=data['stripe_id'])
    merchant.save()
    return Response({"user_id":user.id,"merchant_id":merchant.merchant_id,"status":"success"})

#Login Function
@api_view(['POST'])
def login(request):
    user = auth.authenticate(username=request.data['email'], password=request.data['password'])
    if(user is not None):
        print(auth.login(request, user))
        return Response({"user_id": user.id,"status":"success"})
    else:
        return Response("Invalid username or password.", status=status.HTTP_403_FORBIDDEN)

#Logout Function
@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response("User is logged out.")