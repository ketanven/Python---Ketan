from django.db import models

class Product(models.Model):
    # Primary key for the product, automatically increment
    product_id = models.AutoField(primary_key=True)
    
    # Name of the product with a maximum length of 100 characters
    product_name = models.CharField(max_length=100)

    def __str__(self):
        # Return the product name when the object is represented as a string
        return self.product_name

class ProductSubCategory(models.Model):
    # Foreign key linking to the Product model, with cascading delete
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    # Price of the subcategory with up to 10 digits and 2 decimal places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Optional image field to upload product images
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    
    # Model of the subcategory with a maximum length of 50 characters
    model = models.CharField(max_length=50)
    
    # RAM specification for the subcategory with a maximum length of 50 characters
    ram = models.CharField(max_length=50)

    def __str__(self):
        # Return a string representation of the subcategory, including the product name and model
        return f"{self.product.product_name} - {self.model}"
