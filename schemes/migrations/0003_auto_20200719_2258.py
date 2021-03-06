# Generated by Django 2.2.6 on 2020-07-19 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemes', '0002_remove_stateschemelist_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='centreschemelist',
            name='ministry',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='stateschemelist',
            name='ministry',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='stateschemelist',
            name='state',
            field=models.CharField(choices=[('AP', 'Andhra Pradesh'), ('AR', 'Arunachal Pradesh'), ('AS', 'Assam'), ('BR', 'Bihar'), ('CG', 'Chhattisgarh'), ('GA', 'Goa'), ('GJ', 'Gujarat'), ('HR', 'Haryana'), ('HP', 'Himachal Pradesh'), ('JK', 'Jammu and Kashmir'), ('JH', 'Jharkhand'), ('KA', 'Karnataka'), ('KL', 'Kerala'), ('MP', 'Madhya Pradesh'), ('MH', 'Maharashtra'), ('MN', 'Manipur'), ('ML', 'Meghalaya'), ('MZ', 'Mizoram'), ('NL', 'Nagaland'), ('OD', 'Odisha'), ('PB', 'Punjab'), ('SK', 'Sikkim'), ('TN', 'Tamil Nadu'), ('TS', 'Telangana'), ('TR', 'Tripura'), ('UK', 'Uttrakhand'), ('UP', 'Uttar Pradesh'), ('WB', 'West Bengal'), ('AN', 'Andaman and Nicobar Islands'), ('CH', 'Chandigarh'), ('DN', 'Dadra and Nagar Haveli'), ('DD', 'Daman and Diu'), ('DL', 'Delhi'), ('LH', 'Ladakh')], default=False, max_length=25),
        ),
    ]
