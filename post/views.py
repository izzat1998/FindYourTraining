from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View

from post.models import Post


class PostDelete(View):
    def post(self,request,pk):
        post=Post.objects.get(pk=pk)
        post.delete()
