# Generated by Django 3.2.3 on 2021-06-01 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0008_alter_advertise_adv_datetime_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 10, 15, 56, 345791)),
        ),
    ]
