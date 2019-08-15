from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
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
        return render(request, 'userprofile/user_page.html', context={'user': current_user, 'posts': posts, 'friends': friends})


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'body', )


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post')


class CreatePost(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.save()


# class CreatePost(View):
#     def post(self, request):
#         content = request.POST.get('content')
#         current_user = UserProfile.objects.get(user=request.user)
#         post = Post.objects.create(body=content, author=current_user)
#         return HttpResponseRedirect(reverse('user_page', kwargs={'username': user.username}))
#

class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.post = self.request.POST.get('post_id')
        instance.save()


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
