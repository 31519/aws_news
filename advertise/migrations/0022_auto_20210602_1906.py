# Generated by Django 3.2.3 on 2021-06-02 13:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0021_auto_20210602_1847'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 19, 6, 32, 499109)),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='adv_plan',
            field=models.IntegerField(choices=[(1000, 'Free'), (5000, 'Weeks'), (15000, 'Month')], default='Free', max_length=200),
        ),
    ]