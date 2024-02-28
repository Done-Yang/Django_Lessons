from django.contrib import admin
from .models import Blog, Student

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'update', 'show_image']
    search_fields = ['title']
    list_filter = ['title']

class StudentAdmin(admin.ModelAdmin):
    list_display = ['studentID', 'firstName', 'email', 'showImage']

# Register your models here.
admin.site.register(Blog, BlogAdmin)
admin.site.register(Student, StudentAdmin)