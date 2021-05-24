from django.contrib import admin
from .models import Account, UserProfile
from django.utils.html import format_html
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="30" style="border-radius:50%;">'.format(object.images.url))
    thumbnail.short_description = 'Images'
    list_display = ('thumbnail', 'user', 'address', 'state', 'country')
admin.site.register(Account)
admin.site.register(UserProfile, UserProfileAdmin)