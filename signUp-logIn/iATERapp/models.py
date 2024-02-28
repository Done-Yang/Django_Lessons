from django.db import models
from django.utils.html import format_html
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='media', null=True, blank=True)  # null=True: can complate with none file, value, ..in database # blank=True work in admin page
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def show_image(self):
        if self.image:
            return format_html('<img src="%s" height="50px">' % self.image.url)
        return 'NULL'
    show_image.allow_tags = True

    def __str__(self):
        return self.title




class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    profile = models.ImageField(upload_to='userProfile')
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)
    studentID = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    nickName = models.CharField(max_length=50, null=True, blank=True)

    def showImage(self):
        if self.profile:
            return format_html('<img src="%s" height="auto" width="30px" object-fit="cover" border-radius="30px">' % self.profile.url)
        return 'Null'
    showImage.allow_tags = True

