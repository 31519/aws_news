from django.db import models

from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)
    slug  = models.SlugField(max_length=120, unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, blank=True)
    # cat_img = models.ImageField(upload_to='photos/categories', blank=True)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    
    def get_url(self):
        return reverse('product_by_slug', args=[self.slug])

    # overiding save method to slugify slug area
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.category_name)
    #     super(Category, self).save(*args, **kwargs)


class Posts(models.Model):
    post_name = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    heading = models.CharField(max_length=100, blank=True)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    images = models.ImageField(upload_to="images/posts/", default="images/posts/noimg.jpg")


    def __str__(self):
        return self.post_name

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def get_url(self):
        return reverse('post_detail', args=[self.category.slug, self.slug])
