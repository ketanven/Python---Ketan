from django.urls import path
from .views import (
    PostListCreateView,
    PostRetrieveUpdateDestroyView,
    CommentListCreateView,
    CommentRetrieveUpdateDestroyView
)

urlpatterns = [
    # Post URLs
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),  # List all posts or create a new post
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),  # Retrieve, update, or delete a specific post

    # Comment URLs
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),  # List all comments or create a new comment
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),  # Retrieve, update, or delete a specific comment
]
