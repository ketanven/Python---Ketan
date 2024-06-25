from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    countryName = models.CharField(max_length=20)
    profile = models.ImageField(default="",upload_to="picture/")
    
    
    def __str__(self):
        return self.name
