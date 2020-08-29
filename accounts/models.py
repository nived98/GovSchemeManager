from dateutil.relativedelta import relativedelta
from django.db import models
from django.contrib.auth.models import *
from django.conf import *
# Create your models here.


class CustomUser(AbstractUser):
    # add additional fields in heres
    def __str__(self):
        return self.email


class UserProfile(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    dob = models.DateField(max_length=8, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)

    aadhaar_number = models.BigIntegerField(
        default=False, null=True, blank=True)
    Phone_number = models.BigIntegerField(default=False, null=True, blank=True)
    income = models.IntegerField(default=False, null=True, blank=True)
    x = (
        ('H', 'Hindu'),
        ('M', 'Muslim'),
        ('C', 'Christian'),
        ('S', 'Sikh'),
        ('O', 'Others'),
        ('N', 'NIL'),
    )
    religion = models.CharField(max_length=1, choices=x,
                                null=False, default='N')

    y = (
        ('G', 'General'),
        ('E', 'EWS'),
        ('O', 'OBC'),
        ('SC', 'SC'),
        ('ST', 'ST'),
    )
    caste = models.CharField(max_length=2, choices=y,
                             null=False, default='G')
    address = models.CharField(
        max_length=200, default=False, null=True, blank=True)
    city = models.CharField(
        max_length=100, default=False, null=True, blank=True)
    z = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UK', 'Uttrakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LH', 'Ladakh'),
    )

    state = models.CharField(max_length=25, choices=z,
                             null=False, default=False)
    pincode = models.IntegerField(default=False, null=True, blank=True)
    family_members = models.IntegerField(default=False, null=True, blank=True)

    g = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other'),
    )

    gender = models.CharField(max_length=1, choices=g,
                              null=False, default='M')


class CentreAdminProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_admin = models.BooleanField()
    ministry = models.CharField(
        max_length=50, null=False, blank=False)


class StateAdminProfile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    is_admin = models.BooleanField()
    z = (
        ('AP', 'Andhra Pradesh'),
        ('AR', 'Arunachal Pradesh'),
        ('AS', 'Assam'),
        ('BR', 'Bihar'),
        ('CG', 'Chhattisgarh'),
        ('GA', 'Goa'),
        ('GJ', 'Gujarat'),
        ('HR', 'Haryana'),
        ('HP', 'Himachal Pradesh'),
        ('JK', 'Jammu and Kashmir'),
        ('JH', 'Jharkhand'),
        ('KA', 'Karnataka'),
        ('KL', 'Kerala'),
        ('MP', 'Madhya Pradesh'),
        ('MH', 'Maharashtra'),
        ('MN', 'Manipur'),
        ('ML', 'Meghalaya'),
        ('MZ', 'Mizoram'),
        ('NL', 'Nagaland'),
        ('OD', 'Odisha'),
        ('PB', 'Punjab'),
        ('SK', 'Sikkim'),
        ('TN', 'Tamil Nadu'),
        ('TS', 'Telangana'),
        ('TR', 'Tripura'),
        ('UK', 'Uttrakhand'),
        ('UP', 'Uttar Pradesh'),
        ('WB', 'West Bengal'),
        ('AN', 'Andaman and Nicobar Islands'),
        ('CH', 'Chandigarh'),
        ('DN', 'Dadra and Nagar Haveli'),
        ('DD', 'Daman and Diu'),
        ('DL', 'Delhi'),
        ('LH', 'Ladakh'),
    )

    state = models.CharField(max_length=25, choices=z,
                             null=False)

    ministry = models.CharField(
        max_length=50, null=False, blank=False)
