from django.contrib import admin
from .models import Categories, Advertise, Ads_Payment
# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('categories_adv',)}
    class Meta:
        model = Categories

class AdvertiseAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug': ('adv_heading',)}
    # fields = ['user', 'adv_category', 'adv_heading', 'slug', 'adv_descriptions', 'adv_images', 'adv_conclude', 'adv_created_date', 'adv_updated_date', 'adv_start_date' 'adv_end_date']
    readonly_fields = ['adv_created_date', 'adv_updated_date']
    class Meta:
        model = Advertise
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Advertise, AdvertiseAdmin)
admin.site.register(Ads_Payment)


    