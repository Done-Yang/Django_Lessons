from random import choices
from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE = (
        ('1','Hod'),
        ('2','Active'),
    )
    user_type = models.CharField(choices = USER_TYPE, max_length=50, default=2)
    profile = models.ImageField(upload_to='UserProfile', blank=True, null= True)

class Active(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    cender = models.CharField(max_length = 10)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
