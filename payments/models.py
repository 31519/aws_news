from typing import Tuple
from django.contrib.auth.models import User
from django.db import models
from django.db.models.enums import Choices
from accounts.models import Account
# Create your models here.


PLAN = (
    ('Free', 'Free'),
    (50, 'Days'),
    (150, 'Month'),
)

class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    plan = models.CharField(max_length=200, choices=PLAN, default='Free')
    created_date = models.DateTimeField(auto_now=True)
    order_number = models.IntegerField(blank=True)
    order_id = models.CharField(max_length=200, blank=True)


    def __str__(self):
        return self.plan

class Order(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    order_number = models.IntegerField(blank=True)
    order_id = models.CharField(max_length=200, blank=True)
    order_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment.plan

class Subscribed(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True)
    order= models.ForeignKey(Order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.payment.plan