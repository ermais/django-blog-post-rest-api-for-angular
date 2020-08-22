from rest_framework.serializers import ModelSerializer
from .models import Post
from comment.serializers import CommentSerializer


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'body',
            'comment_count',
            'pub_date',
        ]


class PostDetailSerializer(ModelSerializer):
    comment_set = CommentSerializer(read_only=False,many=True,required=True)    

    class Meta:
        model = Post
        fields = [
            'id',
            'user',
            'title',
            'slug',
            'body',
            'comment_count',
            'pub_date',
            'comment_set',
        ]

class PostEditSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'body'
        ]