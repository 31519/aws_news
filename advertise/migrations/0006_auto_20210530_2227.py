# Generated by Django 3.2.3 on 2021-05-30 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0005_auto_20210528_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 22, 27, 57, 130158)),
        ),
        migrations.AddField(
            model_name='advertise',
            name='adv_display',
            field=models.BooleanField(default=True),
        ),
    ]