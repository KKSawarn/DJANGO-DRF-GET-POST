from django.db import models

# Create your models here.
class Category(models.Model):
    shirt_choice=[
        ("Small","Small"),
         ("Medium","Medium"),
         ("Large","Large"),
         ("XL","XL"),
    ]
    category_id = models.IntegerField(primary_key=True)
    size=models.CharField(choices=shirt_choice ,max_length=10,default=None)
    price= models.DecimalField(max_digits=19, decimal_places=2,default=None)


class Shirt(models.Model):
    item_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=30,default=None)
    fabric=models.CharField(max_length=20,default=None)
    sku=models.CharField(max_length=20,default=None)
    is_imported=models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)


