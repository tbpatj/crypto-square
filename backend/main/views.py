from re import T
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from crypto.qr_code_gen.QRCodeGenerator import QRCodeGenerator
from crypto.wallet_listener.WalletListener import WalletListener
from squareapi.SquareListener import SquareListener

from rest_framework import status
from django.http import HttpResponse, FileResponse
from .models import Merchant
from django.http import HttpResponse
from .models import Merchant, Transaction

from rest_framework.decorators import api_view
from rest_framework.response import Response

import base64
import json
import os
import random

print(os.getcwd())
listener = WalletListener('0x4d999E20B733f8245c908425CD1b0295C8fFB212')
task = listener.run()
new_square_transaction_listener = SquareListener()

def new_order(invoice_id, order_amount_fiat, sq_merchant_id):
    print('looking for %s' % sq_merchant_id)
    print([m.sq_merchant_id for m in list(Merchant.objects.all())])
    txn = Transaction.objects.create(
        owner=Merchant.objects.get(sq_merchant_id=sq_merchant_id),
        state="Just opened.",
        invoice_id=invoice_id,
        order_amount_fiat=order_amount_fiat
    )


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
    #if(type(data["stripe_id"]) == 'int' or data["stripe_id"].isdigit()):
    #data["sq_merchant_id"] = data["stripe_id"] #yeah, i know
    #data["stripe_id"] = 0
    user = User.objects.create_user(body)
    auth.login(request, user)
    print(data)
    merchant = Merchant(user_id=user.id,stripe_id=0,sq_merchant_id=data['stripe_id'])
    merchant.save()
    print("Create transaction.")
    print(merchant.merchant_id)
    #test = Transaction.objects.create(owner=merchant, state='Just oppened.', invoice_id='1234')
    return Response({"user_id":user.id,"merchant_id":merchant.merchant_id,"status":"success"})
    #else:
        #return Response("Oof bad request, you didn't send in a stripe_id that is of a number", status=status.HTTP_403_FORBIDDEN)
    #Create a merchant linked model
    
    

#Login Function
@api_view(['POST'])
def login(request):
    
    user = auth.authenticate(username=request.data['email'], password=request.data['password'])
    if(user is not None):
        print(auth.login(request, user))
        return Response({"user_id": user.id,"status":"success"})
    else:
        print("not a valid user or password")
        return Response("Invalid username or password.", status=status.HTTP_403_FORBIDDEN)

#Logout Function
@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response("User is logged out.")

@api_view(['GET'])
def check_qr_status(request):
    #if we don't have anything yet
    #return Response({"message":"none"})
    print(request.GET.get('merchant_id', ''))
    merchant = Merchant.objects.get(merchant_id=request.GET.get('merchant_id', ''))
    transactions = Transaction.objects.filter(owner=merchant)
    if not transactions:
        return Response({'message': 'No active transaction.'})
    print(transactions.first().state)
    qr_recieved = request.GET.get('qr_recieved', False)
    print(qr_recieved)
    transaction = transactions.first()
    if transaction.state == 'Just opened.' and qr_recieved=='false':
        print('QR Response.')
        # if we know we need to send back a QR code
        #return Response("")
        gen = QRCodeGenerator()
        uid = str(random.randint(1000000, 9999999))
        amount = transaction.order_amount_fiat / 30000
        print(amount)
        r = gen.gen_qr_code('ethereum', '0x4d999E20B733f8245c908425CD1b0295C8fFB212', amount, int(uid))
        # return render()
        # return FileResponse(r, content_type='image/png')
        print(uid)
        uid = '1'+uid
        print(uid)
        transaction.crypto_uid = uid
        transaction.save()
        print(transaction.crypto_uid)
        with open('static/QR.png', 'rb') as imageFile:
            data = base64.b64encode(imageFile.read()).decode()
            response = json.dumps([{'image': data}])
            return HttpResponse(response, content_type = 'text/json')
    elif transaction.state == 'Transaction pending.':
        return Response({'state':transaction.state})
    elif transaction.state == 'Transaction complete.':
        return Response({'state':transaction.state})
    else:
        return Response({'message':'User has not scanned yet.'})
