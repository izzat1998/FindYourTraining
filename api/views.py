from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import PostSerializer, CommentSerializer, ReplySerializer, UserProfileSerializer
from post.models import Post, Comment, Reply
from userprofile.models import UserProfile


class UserProfileGet(ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):

        qs = UserProfile.objects.all()
        query = self.request.GET.get('q')
        print(query)
        if query is not None:
            qs = UserProfile.objects.filter(name__icontains=query)
            print(qs)

        return qs


class UserProfileDetail(APIView):
    lookup_field = 'id'
    serializer_class = UserProfileSerializer
    def get(self, request, id):
        user = UserProfile.objects.get(id=id)
        print(user)
        user_s = UserProfileSerializer(user)
        return Response(user_s.data)


class CreatePost(CreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.save()


class DestroyPost(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PostSerializer


class CreateComment(CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.save()


class DestroyComment(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CommentSerializer


class CreateReply(CreateAPIView):
    serializer_class = ReplySerializer()
    queryset = Reply.objects.all()

    def perform_create(self, serializer):
        instance = serializer.save()
        instance.author = self.request.user.userprofile
        instance.save()


class DestroyReply(DestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ReplySerializer
