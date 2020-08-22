from django.urls import path
from .views import CommentCreateAPIView
from .models import Comment


urlpatterns = [
    path('posts/<int:id>/comment/create/',CommentCreateAPIView.as_view(),name="comment-add")
]