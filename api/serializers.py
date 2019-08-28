from django.http.response import HttpResponseRedirect
from django.urls import reverse
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from post.models import Post, Comment, Reply
from userprofile.models import UserProfile


class UserProfileSerializer(ModelSerializer):
    userprofile_page = SerializerMethodField('get_userprofile_page')

    class Meta:
        model = UserProfile
        fields = ('id', 'name', 'birth_date', 'userprofile_page')

    def get_userprofile_page(self, obj):
        return obj.profile_page_url


class PostSerializer(ModelSerializer):
    delete_url = SerializerMethodField('get_delete_url')

    class Meta:
        model = Post
        fields = ('id', 'body', 'file', 'delete_url')

    def get_delete_url(self, obj):
        return obj.get_delete_url()


class CommentSerializer(ModelSerializer):
    delete_url = SerializerMethodField('get_delete_url')

    class Meta:
        model = Comment
        fields = ('content', 'post', 'delete_url')

    def get_delete_url(self, obj):
        return obj.get_delete_url()


class ReplySerializer(ModelSerializer):
    delete_url = SerializerMethodField('get_delete_url')

    class Meta:
        model = Reply
        fields = ('id', 'content', 'comment', 'delete_url')

    def get_delete_url(self, obj):
        return obj.get_delete_url()
