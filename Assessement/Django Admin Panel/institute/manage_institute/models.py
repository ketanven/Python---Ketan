from django.db import models
from django.utils import timezone
from datetime import date

class Student(models.Model):
    full_name = models.CharField(max_length=200, default='John Doe')
    date_of_birth = models.DateField(default=date(2000, 1, 1))
    date_of_joining = models.DateTimeField(default=timezone.now)
    address = models.TextField(default='123 Main Street')

    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    full_name = models.CharField(max_length=200, default='John Doe')
    date_of_birth = models.DateField(default=date(2000, 1, 1))
    date_of_joining = models.DateTimeField(default=timezone.now)
    address = models.TextField(default='123 Main Street')
    compensation = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Club(models.Model):
    name = models.CharField(max_length=100, default="Default Club Name")
    description = models.TextField(default="Default description")
    founded_date = models.DateField(default=timezone.now)
    president = models.CharField(max_length=200, default="Default President")
    members_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200, default="Untitled")
    author = models.CharField(max_length=200, default="Unknown Author")
    published_date = models.DateField(default=timezone.now)  # Default to today's date
    isbn = models.CharField(max_length=13, unique=True, default="0000000000000")
    pages = models.PositiveIntegerField(default=0)
    language = models.CharField(max_length=20, choices=[('English', 'English'), ('Spanish', 'Spanish'), ('French', 'French')], default='English')

    def __str__(self):
        return self.title



class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    profile = models.ImageField(upload_to="picture/")
    institute = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name