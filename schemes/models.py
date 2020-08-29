from django.db import models

from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
from django.dispatch import receiver
from accounts.models import StateAdminProfile, CentreAdminProfile


class StateSchemeList(models.Model):

    owner = models.ForeignKey(StateAdminProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    overview = models.TextField(max_length=5000, null=False, blank=False)
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
    ministry = models.CharField(
        max_length=50, null=False, blank=False, default=False)
    monetory_benefits = models.IntegerField(default=False)
    slug = models.SlugField(blank=True, unique=True)
    eligibility_criterion = models.TextField(
        max_length=5000, null=False, blank=False)
    max_yearly_income = models.IntegerField(default=False)
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
    BPL = models.BooleanField()

    age = models.IntegerField(default=False)
    family_members = models.IntegerField(default=False)

    g = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other'),
    )

    gender = models.CharField(max_length=1, choices=g,
                              null=False, default='M')
    minority = models.BooleanField()
    # slug = models.SlugField(blank=True, unique=True)


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.owner.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=StateSchemeList)


class CentreSchemeList(models.Model):

    owner = models.ForeignKey(CentreAdminProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    overview = models.TextField(max_length=5000, null=False, blank=False)
    ministry = models.CharField(
        max_length=50, null=False, blank=False, default=False)
    monetory_benefits = models.IntegerField(default=False)
    slug = models.SlugField(blank=True, unique=True)
    eligibility_criterion = models.TextField(
        max_length=5000, null=False, blank=False)
    max_yearly_income = models.IntegerField(default=False)
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
    BPL = models.BooleanField()

    age = models.IntegerField(default=False)
    family_members = models.IntegerField(default=False)

    g = (
        ('M', 'male'),
        ('F', 'female'),
        ('O', 'other'),
    )

    gender = models.CharField(max_length=1, choices=g,
                              null=False, default='M')
    is_admin = models.BooleanField()
    minority = models.BooleanField()
    slug = models.SlugField(blank=True, unique=True)
    # ministry = owner.ministry


def pre_save_blog_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(
            instance.owner.username + "-" + instance.title)


pre_save.connect(pre_save_blog_post_receiver, sender=CentreSchemeList)

# centre scheme manager and state scheme manager
# scheme eligibility seperate table
