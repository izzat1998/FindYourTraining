from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from api.serializers import PostSerializer, CommentSerializer
from post.models import Post, Comment
from userprofile.models import UserProfile


class CreatePost(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.save()


class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.save()


