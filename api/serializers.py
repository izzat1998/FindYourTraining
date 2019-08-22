from rest_framework.serializers import ModelSerializer

from post.models import Post, Comment, Reply


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'body',)


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('content', 'post',)


class ReplySerializer(ModelSerializer):
    class Meta:
        model = Reply
        fields = ('content', 'comment',)
