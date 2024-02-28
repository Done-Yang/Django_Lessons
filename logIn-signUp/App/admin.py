from django.contrib import admin
from .models import CustomUser

class CustomUserAddmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'user_type', 'profile']
    search_filter = ['username']
    prepopulated_field = {'slug': ['name']}
    fieldsets = (
        ()
    )

# Register your models here.
admin.site.register(CustomUser, CustomUserAddmin)