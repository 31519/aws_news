# Generated by Django 3.2.3 on 2021-05-28 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='images',
            field=models.ImageField(blank=True, default='profile.svg', upload_to='userprofile'),
        ),
    ]
