from rest_framework import generics, permissions
from .serializers import CommentSerializer
from .models import Comment

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]
