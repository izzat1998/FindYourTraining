from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import View

from post.models import Post


class PostDelete(View):
    def get(self,request,*args,**kwargs):
        print(self.kwargs['id'])
        post = Post.objects.get(pk=self.kwargs['id'])
        post.delete()
