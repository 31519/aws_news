# Generated by Django 3.2.3 on 2021-05-31 18:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0006_auto_20210530_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 31, 23, 51, 17, 754110)),
        ),
    ]
