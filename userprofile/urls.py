from django.contrib import admin
from django.urls import path, include

from userprofile.views import Home, UserPage

urlpatterns = [

    path('', UserPage.as_view(), name='user_page'),

]
