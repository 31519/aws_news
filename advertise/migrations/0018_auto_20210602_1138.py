# Generated by Django 3.2.3 on 2021-06-02 06:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0017_auto_20210602_1134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads_payment',
            old_name='User',
            new_name='user',
        ),
        migrations.AddField(
            model_name='ads_payment',
            name='adv_plan',
            field=models.CharField(choices=[(2, 'Free'), (50, 'Weeks'), (150, 'Month')], default='Free', max_length=200),
        ),
        migrations.AlterField(
            model_name='advertise',
            name='adv_datetime_now',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 2, 11, 38, 28, 213916)),
        ),
    ]