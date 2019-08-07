from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from post.models import Post, Comment
from userprofile.models import UserProfile


class Login(View):
    def post(self, request):
        name = request.POST.get('username')
        password2 = request.POST.get('password')
        print(name)
        print(password2)
        if name and password2:
            user = User.objects.get(username=name)
            if user.check_password(password2):
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return HttpResponseRedirect(reverse('user_page', kwargs={'username': user.username}))
        return HttpResponse("WTF")


class UserPage(View):
    def get(self, request, username):
        current_user = UserProfile.objects.get(user=request.user)
        posts = Post.objects.filter(author=current_user)
        all_users = UserProfile.objects.all()
        return render(request, 'userprofile/user_page.html', context={'user': current_user, 'posts': posts})

    def post(self, request, username):
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
        return HttpResponseRedirect(reverse('user_page', kwargs={'username': request.user.username}))


class Home(TemplateView):
    template_name = 'userprofile/page-login.html'
