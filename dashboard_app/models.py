from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rent(models.Model):
    rent_month = models.CharField(max_length=150)
    rent_year = models.CharField(max_length=150)
    rent_amount = models.DecimalField(max_digits = 7,decimal_places = 2)
    electric_amount = models.DecimalField(max_digits = 7,decimal_places = 2)
    water_amount = models.DecimalField(max_digits = 7,decimal_places = 2)
    wifi_amount = models.DecimalField(max_digits = 7,decimal_places = 2)
    other_amount = models.DecimalField(max_digits = 7,decimal_places = 2)
    other_desc = models.CharField(max_length=300)


class UserProfile(models.Model):
    user_profile_full_name = models.CharField(max_length=512)
    user_profile_short_name = models.CharField(max_length=255)
    user_profile_phone_number = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
