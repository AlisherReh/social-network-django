from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Status(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE) 
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    profile_picture = models.ImageField(null=True, blank=True, default='123_fvipp2r.png')
    bio = models.TextField(null=True)
    country = models.CharField(max_length=70, null=True)
    phone = models.CharField(max_length=70, null=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

class Friends(models.Model):
    friend_status = models.CharField(max_length=10, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)


