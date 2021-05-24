from django.contrib import admin
from .models import Category, Posts
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    class Meta:
        model = Category


class PostsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('post_name',)}
    class Meta:
        model = Posts


admin.site.register(Category, CategoryAdmin)
admin.site.register(Posts, PostsAdmin)