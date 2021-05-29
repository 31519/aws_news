from django.contrib import admin
from .models import Account, UserProfile, WriteToUs
from django.utils.html import format_html

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'address', 'state', 'country']
admin.site.register(Account)
admin.site.register(WriteToUs)
admin.site.register(UserProfile, UserProfileAdmin)