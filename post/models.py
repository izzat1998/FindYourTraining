from django.db import models
from django.urls import reverse

from userprofile.models import UserProfile




class Post(models.Model):
    body = models.TextField( blank=True, null=True)
    file = models.FileField(upload_to='media/', blank=True,null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-date_pub', ]

    def __str__(self):
        return self.body or ""


    def get_delete_url(self):
        return reverse("post-delete", kwargs={'pk': self.id})


class Comment(models.Model):
    content = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)

    class Meta:
        ordering = ['-date_pub', ]

    def __str__(self):
        return self.content

    def get_delete_url(self) -> str:
        return reverse("comment-delete", kwargs={'pk': self.id})


class Reply(models.Model):
    content = models.TextField(blank=True, null=True)
    date_pub = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.content

    def get_delete_url(self) -> str:
        return reverse("reply-delete", kwargs={'pk': self.id})

