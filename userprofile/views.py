from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from post.models import Post, Comment
from userprofile.models import UserProfile


class UserPage(View):
    def get(self, request):
        current_user = UserProfile.objects.get(user=request.user)
        posts = Post.objects.filter(author=current_user)
        return render(request, 'userprofile/user_page.html', context={'user': current_user, 'posts': posts})

    def post(self, request):
        # CreatePost
        content = request.POST.get('post_content')
        current_user = UserProfile.objects.get(user=request.user)
        Post.objects.create(body=content, author=current_user)
        posts = Post.objects.filter(author=current_user)
        return render(request, 'userprofile/user_page.html', context={'user': current_user, 'posts': posts})


class PostComment(View):
    def post(self, request, pk):
        content_comment = request.POST.get('post_comment')
        current_post = Post.objects.get(pk=pk)
        current_user = UserProfile.objects.get(user=request.user)
        Comment.objects.create(content=content_comment, post=current_post, author=current_user)
        return redirect('user_page')



class Home(TemplateView):
    template_name = 'userprofile/page-login.html'
