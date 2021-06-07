from django.contrib import admin

# Register your models here.
from .models import Number, Again
admin.site.register(Number)
admin.site.register(Again)