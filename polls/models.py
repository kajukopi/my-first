import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin

class Blog(models.Model):
    blog_text = models.CharField(max_length=200)
    blog_subject = models.CharField(max_length=1000)
    blog_date = models.DateTimeField('blog published')
    
    @admin.display(
            boolean=True,
            ordering='blog_date',
            description='Published recently?',
        )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.blog_date <= now

class Choice(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

