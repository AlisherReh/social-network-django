from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 

from .views import ( 
    profile_view, 
    my_profile_view, 
    profiles_list_view, 
    edit_status_view,
    follow_func,
    postDelete
)


app_name = 'profiles'

urlpatterns = [
    path('', profiles_list_view, name='profile-detail-view'),
    path('myprofile/', my_profile_view, name='my-profile-view'),
    path('myprofile/edit/', edit_status_view, name='edit-status-view'),
    path('myprofile/postDelete/<int:id>', postDelete, name='postDelete'),
    path('profile/<int:id>', profile_view, name='profile-view'),
    path('profile/follow/<int:id>', follow_func, name='follow_func')
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)