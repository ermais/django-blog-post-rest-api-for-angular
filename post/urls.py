from django.urls import path
from .views import PostListAPIView, PostCreateAPIView,PostDetailAPIView,PostUpdateAPIView


urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name="post-list"),
    path('posts/create/', PostCreateAPIView.as_view(), name="post-create"),
    path('posts/<str:slug>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('posts/<str:slug>/edit/',PostUpdateAPIView.as_view(),name='post-edit'),
]
