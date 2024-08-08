from django.urls import path
from .views import (
    post_list_create_view,
    post_retrieve_update_destroy_view,
    comment_list_create_view,
    comment_retrieve_update_destroy_view
)

urlpatterns = [
    # Post URLs
    path('posts/', post_list_create_view, name='post-list-create'),  # List all posts or create a new post
    path('posts/<int:pk>/', post_retrieve_update_destroy_view, name='post-detail'),  # Retrieve, update, or delete a specific post

    # Comment URLs
    path('comments/', comment_list_create_view, name='comment-list-create'),  # List all comments or create a new comment
    path('comments/<int:pk>/', comment_retrieve_update_destroy_view, name='comment-detail'),  # Retrieve, update, or delete a specific comment
]
