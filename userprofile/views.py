from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from requests import Response
from rest_framework.generics import CreateAPIView
from rest_framework.serializers import ModelSerializer

from post.models import Post, Comment
from userprofile.models import UserProfile, Friend


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
        return HttpResponse("Not working")


class UserPage(View):
    def get(self, request, username):
        current_user = UserProfile.objects.get(user=request.user)
        posts = Post.objects.filter(author=current_user)
        friends = UserProfile.objects.all()
        return render(request, 'userprofile/user_page.html',
                      context={'user': current_user, 'posts': posts, 'friends': friends})


# class UserFriends(View):
#     def get(self, request, username):
#         first_name = request.GET.get('first_name')
#         country = request.GET.get('country')
#         print(first_name, country)
#         return render(request, 'userprofile/user_friends.html', context={'username': username})


class UserFriends(ListView):
    template_name = 'userprofile/user_friends.html'
    context_object_name = 'users'

    def get_queryset(self):
        print("1")
        qs = UserProfile.objects.filter()
        first_name = self.request.GET.get('first_name')
        country = self.request.GET.get('country')
        print(first_name, country)
        if first_name:
            qs = qs.filter(name=first_name)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["vars"] = self.request.GET
        return context


# class CreatePost(View):
#     def post(self, request):
#         content = request.POST.get('content')
#         current_user = UserProfile.objects.get(user=request.user)
#         post = Post.objects.create(body=content, author=current_user)
#         return HttpResponseRedirect(reverse('user_page', kwargs={'username': user.username}))
#


class SendRequest(View):
    def get(self, request, pk):
        return HttpResponseRedirect(reverse('user_page', kwargs={'username': request.user.username}))


class PostComment(View):
    def post(self, request, pk):
        content_comment = request.POST.get('post_comment')
        current_post = Post.objects.get(pk=pk)
        print(current_post)
        current_user = UserProfile.objects.get(user=request.user)
        Comment.objects.create(content=content_comment, post=current_post, author=current_user)
        return HttpResponseRedirect(reverse('user_page', kwargs={'username': request.user.username}))


class Home(TemplateView):
    template_name = 'userprofile/page-login.html'
