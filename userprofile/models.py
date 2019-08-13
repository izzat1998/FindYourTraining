from django.contrib.auth.models import User
from django.db import models


class Requests(models.Model):
    sender = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey('UserProfile', on_delete=models.CASCADE, related_name='receiver')


class UserProfile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Friend(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True)
    friend = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, related_name='friendname')

    def __str__(self):
        return self.user.name + ' <-> ' + self.friend.name

