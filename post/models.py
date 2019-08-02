from django.db import models

from userprofile.models import UserProfile


class Post(models.Model):
    body = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    author = models.OneToOneField(UserProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.author
