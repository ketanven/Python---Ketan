from django.contrib import admin
from .models import Student, Teacher, Club, Book, User

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Club)
admin.site.register(Book)
admin.site.register(User)

