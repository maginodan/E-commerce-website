from django.db import models

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.name 
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=200)
    # can be blank because of the products have may not have images
    image = models.ImageField(blank=True, upload_to='images')
