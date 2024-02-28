from django.contrib import admin

from .models import Profile, Skill, Experian, Comment

class CommentTabularinline(admin.TabularInline):
    model = Comment
    extra = 2

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['showpictur', 'name', 'selfExplain', 'title', 'describtion']
    inlines = [CommentTabularinline]

class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'detial']


# Register your models here.
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experian)

