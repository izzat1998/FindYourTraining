from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name