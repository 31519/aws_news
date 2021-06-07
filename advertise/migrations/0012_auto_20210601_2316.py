# Generated by Django 3.1.5 on 2021-06-01 17:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0011_auto_20210601_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertise',
            name='adv_plan',
            field=models.CharField(choices=[('Free', 'Free'), ('Weeks', '50'), ('Month', '150')], default='Free', max_length=200),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 1, 23, 16, 8, 350085)),
        ),
    ]