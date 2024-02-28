from django.db import models
from django.utils.html import format_html

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 50)
    selfExplain = models.CharField(max_length=250, blank=True, null=True)
    picture = models.ImageField(upload_to = '')
    title = models.CharField(max_length = 500)
    describtion = models.TextField()

    def showpictur(self):
        if self.picture:
            return format_html('<img src="%s" height="auto" width="80px" object-fit="cover" border-radius="30px">' % self.picture.url)
        else:
            return 'Null'
    showpictur.allow_tags = True

    def det_comment_count(self):
        return self.comment_set.count()
    
class Skill(models.Model):
    icon = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length = 100)
    detial = models.TextField()
    performance = models.CharField(max_length = 5000, blank = True, null = True)

class Experian(models.Model):
    title = models.CharField(max_length = 100)
    expr_month = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.title}-{self.expr_month}'

class Comment(models.Model):
    where = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)
    ratting = models.IntegerField(default=0, blank=True, null=True)

    class Meta:
        ordering = ['-id']
        verbose_name_plural = ['comment']

    def __str__(self):
        return self.comment
