from django.db import models
from accounts.models import Account
from django.urls import reverse
# Create your models here.
class Categories(models.Model):
    categories_adv = models.CharField(max_length=100, unique=True)
    slug  = models.SlugField(max_length=100)
    created_date  = models.DateField(auto_now_add=True)
    updated_date  = models.DateField(auto_now=True)

    
    class Meta:
        verbose_name = "adv_category"
        verbose_name_plural = "adv_categories"

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
    adv_start_date = models.DateField(auto_now_add=True, blank=True)
    adv_end_date = models.DateField(auto_now_add=True, blank=True)
    

    def __str__(self):
        return self.adv_heading

    def get_url(self):
        return reverse('advertise_detail', args=[self.adv_category.slug, self.slug])

