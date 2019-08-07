from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    receiver = models.IntegerField(blank=True,default=0)

    def __str__(self):
        return self.name

class Friend(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True)
    friend = models.ForeignKey(UserProfile,on_delete=models.CASCADE,blank=True ,related_name='friendname')