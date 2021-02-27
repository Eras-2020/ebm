from django.db import models
from .category import Category
from ckeditor_uploader.fields import RichTextUploadingField


class Product(models.Model):
    SIZE = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Extra Large', 'Extra Large'),
    )
    QUANTITY = (
        ('1/2Kg', '1/2Kg'),
        ('1Kg', '1Kg'),
        ('1/2L', '1/2L'),
        ('1L', '1L'),
    )
    COLOR = (
        ('Blue', 'Blue'),
        ('Black', 'Black'),
        ('Red', 'Red'),
        ('White', 'White'),
        ('Yellow', 'Yellow'),
        ('Orange', 'Orange'),
        ('Purple', 'Purple'),
        ('Green', 'Green'),
        ('Gray', 'Gray'),
    )
    STOCK = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)
    in_stock = models.BooleanField(default=False)
    product_stock_quantity = models.IntegerField(default=0)
    brand = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, choices=SIZE, blank=True)
    quantity = models.CharField(max_length=100, choices=QUANTITY, blank=True)
    color = models.CharField(max_length=100, choices=COLOR, blank=True)
    description = RichTextUploadingField(blank=True)
    delivery_time = RichTextUploadingField(blank=True)
    image = models.ImageField(upload_to='products/')
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)


class ProductImages(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image_add = models.ImageField(upload_to='products/', blank=True)
