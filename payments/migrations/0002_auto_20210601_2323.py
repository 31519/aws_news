# Generated by Django 3.1.5 on 2021-06-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='plan',
            field=models.CharField(choices=[('Free', 'Free'), (50, 'Days'), (150, 'Month')], default='Free', max_length=200),
        ),
    ]
