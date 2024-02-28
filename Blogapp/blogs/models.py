from django.db import models
from django.utils.html import format_html
from categories.models import Category


# Create your models here.
class Blogs(models.Model):
    name = models.CharField(max_length=255)
    dsc = models.TextField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    writer = models.CharField(max_length=255)
    views = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog-image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def showimage(self):
        if self.image:
           return format_html('<img src="%s" height="auto", width="50px", object-fit: cover;>' % self.image.url)
        else:
            return 'Null'