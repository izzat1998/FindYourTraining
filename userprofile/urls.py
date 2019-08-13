from django.contrib import admin
from django.urls import path, include

from userprofile.views import Home, UserPage, PostComment, Login, CreatePost

urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('comment/create/<int:pk>', PostComment.as_view(), name='post_comment'),
    path('create/post', CreatePost.as_view(), name='create_post'),
    path('<str:username>', UserPage.as_view(), name='user_page'),
]
