# Generated by Django 3.1.5 on 2021-06-01 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0012_auto_20210601_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 23, 23, 51, 583566)),
        ),
    ]
