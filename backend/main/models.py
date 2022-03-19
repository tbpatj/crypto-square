from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin



# Create your models here.
class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    stripe_id = models.IntegerField()
    sq_api_token = models.CharField(max_length=120)
    sq_merchant_id = models.CharField(max_length=120)
    sq_location_id = models.CharField(max_length=120)

class Transaction(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Merchant, on_delete=models.CASCADE)
    state = models.CharField(max_length=120)
    invoice_id = models.CharField(max_length=120)
    order_amount_fiat = models.FloatField(null=True)
    crypto_amount_eth = models.FloatField(null=True)
    crypto_txn_hash = models.CharField(max_length=120,null=True)
    crypto_uid = models.CharField(max_length=120,null=True)
    exchange_amount_fiat = models.FloatField(null=True)
    exchange_sale_id = models.CharField(max_length=120,null=True)
    plaid_access_token = models.CharField(max_length=120,null=True)
    plaid_txn_id = models.CharField(max_length=120,null=True)
