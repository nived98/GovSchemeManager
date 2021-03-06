# Generated by Django 2.2.6 on 2020-04-08 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(blank=True, max_length=8, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('aadhaar_number', models.BigIntegerField(blank=True, default=False, null=True)),
                ('Phone_number', models.BigIntegerField(blank=True, default=False, null=True)),
                ('income', models.IntegerField(blank=True, default=False, null=True)),
                ('religion', models.CharField(choices=[('H', 'Hindu'), ('M', 'Muslim'), ('C', 'Christian'), ('S', 'Sikh'), ('O', 'Others'), ('N', 'NIL')], default='N', max_length=1)),
                ('caste', models.CharField(choices=[('G', 'General'), ('E', 'EWS'), ('O', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], default='G', max_length=2)),
                ('address', models.CharField(blank=True, default=False, max_length=200, null=True)),
                ('city', models.CharField(blank=True, default=False, max_length=100, null=True)),
                ('state', models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UK', 'Uttrakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LH', 'Ladakh')], default=False, max_length=25)),
                ('pincode', models.IntegerField(blank=True, default=False, null=True)),
                ('family_members', models.IntegerField(blank=True, default=False, null=True)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female'), ('O', 'other')], default='M', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
