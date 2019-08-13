from django.db import models

from userprofile.models import UserProfile


class Post(models.Model):
    body = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering =['-date_pub', ]

    def __str__(self):
        return self.body or ""


class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ['-date_pub', ]

    def __str__(self):
        return self.content
