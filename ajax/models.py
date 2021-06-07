from django.db import models
from accounts.models import Account
# Create your models here.
class Number(models.Model):
    user  = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    date  = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user

class Again(models.Model):
    user  = models.ForeignKey(Account, on_delete=models.CASCADE)
    number = models.IntegerField(blank=True, null=True)
    date  = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.user.first_name



