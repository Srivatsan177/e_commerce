from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class Product(models.Model):
    product_category = models.ForeignKey(ProductCategory, on_delete=models.SET_DEFAULT, default=-1)
    name = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100, default="none")
    color = models.CharField(max_length=30, default="none")

    def __str__(self):
        return f"{self.name}"
    
    def short_description(self):
        return f"{self.description[:100]}..."

class ProductDetail(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.SET_DEFAULT, default=-1)
    serial_number = models.IntegerField(unique=True)
    cost = models.DecimalField(max_digits=100,decimal_places=2)
    is_sold = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.serial_number} - {self.cost} - {self.is_sold}"


class ProductImage(models.Model):
    product_id = models.ForeignKey(ProductDetail, on_delete=models.SET_DEFAULT, default=-1)
    image_s3_location = models.CharField(max_length=500)
