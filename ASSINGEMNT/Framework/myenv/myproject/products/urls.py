from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('create/', views.product_sub_category_create, name='product_sub_category_create'),
    path('update/<int:pk>/', views.product_sub_category_update, name='product_sub_category_update'),
    path('delete/<int:pk>/', views.product_sub_category_delete, name='product_sub_category_delete'),
]
