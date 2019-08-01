from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from authorization.views import login, home

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", home, name="home"),
]
