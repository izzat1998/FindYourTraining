from django.contrib import admin
from django.urls import path, include

from userprofile.views import Home, UserPage, PostComment

urlpatterns = [

    path('', UserPage.as_view(), name='user_page'),
    path('comment/create/<int:pk>', PostComment.as_view(), name='post_comment'),

]
