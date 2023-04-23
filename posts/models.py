from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post_body = models.TextField(null=True)
    image = models.ImageField(blank=True, null=True) 
    video = models.FileField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Comments(models.Model):
    comment_body = models.TextField()
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Likes(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

