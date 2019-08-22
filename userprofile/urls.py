from django.contrib import admin
from django.urls import path, include

from api.views import CreatePost, CreateComment, DestroyPost
from post.views import PostDelete
from userprofile.views import Home, UserPage, Login, UserFriends

urlpatterns = [

    path('login/', Login.as_view(), name='login'),
    path('comment/create/', CreateComment.as_view(), name='create_comment'),
    path('create/post/', CreatePost.as_view(), name='create_post'),
    path('<str:username>/', UserPage.as_view(), name='user_page'),
    path('<str:username>/friends/', UserFriends.as_view(), name='user-friends'),
    path('post/<int:pk>/delete/',DestroyPost.as_view(),name='post-delete'),
]
