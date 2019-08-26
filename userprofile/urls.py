from django.contrib import admin
from django.urls import path, include

from api.views import CreatePost, CreateComment, DestroyPost, DestroyComment, DestroyReply, CreateReply
from userprofile.views import Home, UserPage, Login, UserFriends

urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('<str:username>/', UserPage.as_view(), name='user_page'),
    path('<str:username>/friends/', UserFriends.as_view(), name='user-friends'),


    path('comment/create/', CreateComment.as_view(), name='create_comment'),
    path('post/create/', CreatePost.as_view(), name='create_post'),
    path('reply/create/', CreateReply.as_view(), name='create_reply'),
    path('post/<int:pk>/delete/', DestroyPost.as_view(), name='post-delete'),
    path('comment/<int:pk>/delete/', DestroyComment.as_view(), name='comment-delete'),
    path('reply/<int:pk>/delete/', DestroyReply.as_view(), name='reply-delete'),
]
