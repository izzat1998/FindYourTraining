from django.contrib import admin

# Register your models here.
from post.models import Post, Comment, Reply
from userprofile.models import Friend

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Friend)
admin.site.register(Reply)




# fyt
# git init
# git remote add origin https://github.com/izzat1998/FindYourTraining.git
# git pull origin master
#
#
##
##
