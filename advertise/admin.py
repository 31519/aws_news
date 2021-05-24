from django.contrib import admin
from .models import Categories, Advertise
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('categories_adv',)}
    class Meta:
        model = Categories

class AdvertiseAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('adv_heading',)}
    class Meta:
        model = Advertise
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Advertise, AdvertiseAdmin)