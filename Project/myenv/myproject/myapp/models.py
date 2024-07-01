from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    mobile = models.BigIntegerField()
    countryName = models.CharField(max_length=20)
    profile = models.ImageField(default="",upload_to="picture/")
    usertype = models.CharField(max_length=20,default="buyer")
    
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    category = (
        ("Sofa","Sofa"),
        ("Coffee Table","Coffee Table"),
        ("TV Stand","TV Stand"),
        ("Armchair","Armchair"),
        ("Bookshelf","Bookshelf"),
        ("Bed Frame","Bed Frame"),
        ("Mattress","Mattress"),
        ("Mirror","Mirror"),
        ("Dining Table","Dining Table"),
        ("Sideboard","Sideboard"),
        ("Server Table","Server Table"),
        ("Dining Chairs","Dining Chairs"),
        
    )
    pcategory = models.CharField(max_length=50,choices=category)
    productname = models.CharField(max_length=50)
    pprice = models.PositiveIntegerField()
    pdesc = models.TextField()
    productimage = models.ImageField(default="", upload_to="picture/pimages")
    
    def __str__(self):
        return self.productname
    

