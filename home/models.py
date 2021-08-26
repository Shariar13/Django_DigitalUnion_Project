from django.db import models
from django.db.models.fields import TextField
from django.db.models.fields.files import ImageField
from django.shortcuts import render,redirect,HttpResponseRedirect,reverse
from django.contrib.auth.models import User
from django.conf import settings
from ckeditor.fields import RichTextField





# post
class post(models.Model):
    status=TextField()
    date=models.DateTimeField(auto_now_add=True)
    author_name=models.CharField(max_length=19)
    author_email=models.CharField(max_length=100,null=True)
    post_author=models.CharField(max_length=100,null=True)
    date=models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        if len(self.status)>50:
            return self.status[:50]+"..."
        return self.status

    def get_absolute_url(self):
        return reverse("edit", kwargs={"pk": self.pk})

# comment
class comment(models.Model):
    comment=models.TextField()
    commenter_name=models.CharField(max_length=19)
    commenter_username=models.CharField(max_length=19)
    comment_date=models.DateTimeField(auto_now_add=True)
    comment_id=models.IntegerField(default=-1)
    post_author_name=models.CharField(max_length=99)
    
    def __str__(self):
        if len(self.comment)>50:
            return self.comment[:50]+"..."
        return self.comment

class complain (models.Model):
    name=models.CharField(max_length=19)
    phone=models.CharField(max_length=19)
    village=models.CharField(max_length=19)
    word=models.CharField(max_length=19)
    complain=models.CharField(max_length=9000)
    
    def __str__(self):
        if len(self.complain)>50:
            return self.complain[:50]+"..."
        return self.complain
