from django.contrib import admin
from .models import Post, Comments
from profiles.models import Status
# Register your models here.


admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Status)
