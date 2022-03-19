from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin



# Create your models here.
class Merchant(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    stripe_id = models.IntegerField()
