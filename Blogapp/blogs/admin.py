from django.contrib import admin
from .models import Blogs

class BlogsAdmin(admin.ModelAdmin):
    list_display = ['showimage', 'category', 'name', 'writer']

# Register your models here.
admin.site.register(Blogs, BlogsAdmin)