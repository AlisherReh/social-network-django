from django.urls import path
from .views import posts_page, following_posts_page, save_comment
from django.conf import settings
from django.conf.urls.static import static 
app_name = 'posts'

urlpatterns = [
    path('', posts_page, name='posts'),
    path('following', following_posts_page, name='following'),
    path('save-comment', save_comment, name='save-comment'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)