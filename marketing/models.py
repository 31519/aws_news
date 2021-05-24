from django.db import models
from django.conf import settings
from accounts.models import Account
from django.db.models.signals import post_save

# Create your models here.
class MarketingPreference(models.Model):
    user        = models.OneToOneField(Account, on_delete=models.CASCADE)
    subscribe   = models.BooleanField(default=True)
    mailchimp_msg = models.TextField(null=True, blank=True)
    timestamp     = models.DateTimeField(auto_now_add=True)
    update     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email


def make_marketing_update_reciever(sender, instance, created, *args, **kwargs):
    if created:
        print("Updating email to MailChimps")
post_save.connect(make_marketing_update_reciever, sender=MarketingPreference)


def make_marketing_pref_reciever(sender, instance, created, *args, **kwargs):
    """
    user models
    """
    if created:
        MarketingPreference.objects.get_or_create(user=instance)
post_save.connect(make_marketing_pref_reciever, sender=Account)
    

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
