# Generated by Django 3.2.3 on 2021-06-04 16:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0031_alter_advertise_adv_datetime_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 4, 21, 43, 6, 865164)),
        ),
    ]
