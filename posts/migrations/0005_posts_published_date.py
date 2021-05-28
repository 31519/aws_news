# Generated by Django 3.2.3 on 2021-05-28 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20210519_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='published_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
