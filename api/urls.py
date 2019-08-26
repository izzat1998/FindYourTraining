from django.urls import path

from api.views import UserProfileGet, UserProfileDetail


urlpatterns = [
    path('users_list/<int:id>/', UserProfileDetail.as_view(), name='get_users_detail'),
    path('users_list/', UserProfileGet.as_view(), name='get_users'),
]
