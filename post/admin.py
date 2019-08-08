from django.contrib import admin

# Register your models here.
from post.models import Post, Comment
from userprofile.models import Friend

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friend)
print("hello Aziza")
