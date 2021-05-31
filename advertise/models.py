import datetime
from django.db import models
from accounts.models import Account
from django.urls import reverse
from django.db.models.signals import post_save, pre_save
from django.utils.text import slugify
from datetime import datetime
# Create your models here.
class Categories(models.Model):
    categories_adv = models.CharField(max_length=100, unique=True)
    slug  = models.SlugField(max_length=100)
    created_date  = models.DateField(auto_now_add=True)
    updated_date  = models.DateField(auto_now=True)

    def __str__(self):
        return self.categories_adv

    
    class Meta:
        verbose_name = "adv_category"
        verbose_name_plural = "adv_categories"

def pre_cat_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.categories_adv)

pre_save.connect(pre_cat_slug, sender=Categories)

class Advertise(models.Model):
    adv_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    adv_heading = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100)
    adv_descriptions = models.TextField(max_length=500, blank=True)
    adv_images = models.ImageField(upload_to='images/adv/', default='images/adv/no_img.jpg/')
    adv_conclude = models.CharField(max_length=100, blank=True)
    adv_created_date = models.DateField(auto_now=True)
    adv_updated_date = models.DateField(auto_now_add=True)
    adv_start_date = models.DateField(blank=True)
    adv_end_date = models.DateField( blank=True)


    adv_datetime_now = models.DateTimeField(default=datetime.now())
    adv_display = models.BooleanField(default=True)

    # def timeperiod(self):
    #     from datetime import datetime, timedelta
    #     now = self.adv_datetime_now
    #     data = now + timedelta(days=1)
    #     if (datetime.now()) >= data:
    #         self.adv_display = "False"
    #         print("False")
    #     else:
    #         print("True")



    def __str__(self):
        return self.adv_heading

    def get_url(self):
        return reverse('advertise_detail', args=[self.adv_category.slug, self.slug])


def pre_slug(instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.adv_category)

pre_save.connect(pre_slug, sender=Advertise)