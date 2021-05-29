from django.db import models

# Create your models here.
class AboutUs(models.Model):
    images = models.ImageField(default='my_pic.jpg', blank=True, upload_to='about_us')
    full_name = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    age = models.IntegerField()
    address = models.CharField(max_length=200, blank=True)
    establish = models.DateField(blank=True)

    def __str__(self):
        return self.full_name