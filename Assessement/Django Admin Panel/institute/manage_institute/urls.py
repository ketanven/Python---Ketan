from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('create/', views.create, name='create'),
    path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('tcreate/', views.create_teacher, name='create_teacher'),
    path('tedit/<int:id>/', views.edit_teacher, name='edit_teacher'),
    path('tdelete/<int:id>/', views.delete_teacher, name='delete_teacher'),
    
    path('clubs/', views.club_list, name='club_list'),
    path('clubs/new/', views.create_club, name='create_club'),
    path('clubs/<int:id>/edit/', views.edit_club, name='edit_club'),
    path('clubs/<int:id>/delete/', views.delete_club, name='delete_club'),
    
    path('books/', views.book_list, name='book_list'),
    path('books/new/', views.create_book, name='create_book'),
    path('books/<int:id>/edit/', views.edit_book, name='edit_book'),
    path('books/<int:id>/delete/', views.delete_book, name='delete_book'),

    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('fpass/', views.fpass, name='fpass'),
    path('profilepage/', views.profilepage, name='profilepage'),

    






]
